import requests
import urllib
from .exceptions import crash_handler

class Request:
    # 类变量，共享 session、apikey 和 token
    mcsm_url = None  # 默认值为 None
    timeout = 10  # 默认超时时间
    session = requests.Session()  # 所有实例共享同一个 session
    apikey = None  # 所有实例共享同一个 apikey
    token = None  # 所有实例共享同一个 token

    @staticmethod
    def set_mcsm_url(url):
        """设置类级别的 mcsm_url"""
        Request.mcsm_url = url

    @staticmethod
    def set_timeout(timeout):
        """设置类级别的 timeout"""
        Request.timeout = timeout

    @staticmethod
    def set_apikey(apikey):
        """设置类级别的 apikey"""
        Request.apikey = apikey

    @staticmethod
    def set_token(token):
        """设置类级别的 token"""
        Request.token = token

    def __init__(self, mcsm_url=None, timeout=None):
        """初始化时使用类变量，或者使用传入的参数覆盖默认值"""
        self.mcsm_url = mcsm_url or Request.mcsm_url
        self.timeout = timeout or Request.timeout

    @crash_handler
    def send(self, method, endpoint, params=None, data=None):
        """发送 HTTP 请求"""
        if params is None:
            params = {}
        if not isinstance(endpoint, str):
            endpoint = str(endpoint)
        
        url = urllib.parse.urljoin(self.mcsm_url, endpoint)  # 构建 URL

        # 如果存在 apikey 和 token，加入请求参数
        if Request.apikey is not None:
            params["apikey"] = Request.apikey
        if Request.token is not None:
            params["token"] = Request.token

        # 发起请求
        return Request.session.request(
            method.upper(),
            url,
            params=params,
            data=data,
            timeout=self.timeout,
        )

send = Request().send
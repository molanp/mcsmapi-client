from typing import Any
import requests
import urllib.parse
from mcsmapi.exceptions import MCSMError

class Request:
    mcsm_url = ""
    timeout = 5
    session = requests.Session()
    apikey = None
    token = None

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

    def send(self, method, endpoint, params=None, data=None) -> Any:
        """发送 HTTP 请求"""
        if params is None:
            params = {}
        if data is None:
            data = {}
        if not isinstance(endpoint, str):
            endpoint = str(endpoint)
        
        url = urllib.parse.urljoin(self.mcsm_url, endpoint)
        if Request.apikey is not None:
            params["apikey"] = Request.apikey
            data["apikey"] = Request.apikey
        if Request.token is not None:
            params["token"] = Request.token
            data["token"] = Request.token

        response =  Request.session.request(
            method.upper(),
            url,
            params=params,
            data=data,
            timeout=self.timeout,
        )
        try:
            response.raise_for_status()
            return response.json()["data"]
        except requests.exceptions.HTTPError as e:
            raise MCSMError(response.status_code, response.json().get("data", response.text)) from e

send = Request().send
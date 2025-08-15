from typing import Any
import requests
import urllib.parse

from mcsmapi.pool import ApiPool
from .exceptions import MCSMError


class Request:
    mcsm_url: str = ""
    timeout: int = 5
    session = requests.Session()
    apikey: str | None = None
    token: str | None = None

    @classmethod
    def set_mcsm_url(cls, url: str):
        """设置类级别的 mcsm_url"""
        cls.mcsm_url = url

    @classmethod
    def set_timeout(cls, timeout: int):
        """设置类级别的 timeout"""
        cls.timeout = timeout

    @classmethod
    def set_apikey(cls, apikey: str):
        """设置类级别的 apikey"""
        cls.apikey = apikey

    @classmethod
    def set_token(cls, token: str):
        """设置类级别的 token"""
        cls.token = token

    @classmethod
    def __init__(cls, mcsm_url: str | None = None, timeout: int | None = None):
        """初始化时使用类变量，或者使用传入的参数覆盖默认值"""
        cls.mcsm_url = mcsm_url or cls.mcsm_url
        cls.timeout = timeout or cls.timeout

    @classmethod
    def send(
        cls,
        method: str,
        endpoint: str | ApiPool,
        params: dict | None = None,
        data: Any | None = None,
    ) -> Any:
        """发送 HTTP 请求"""
        if params is None:
            params = {}
        if data is None:
            data = {}
        if isinstance(endpoint, ApiPool):
            endpoint = endpoint.value

        url = urllib.parse.urljoin(cls.mcsm_url, endpoint)
        if cls.apikey is not None:
            params["apikey"] = cls.apikey
        if cls.token is not None:
            params["token"] = cls.token

        response = cls.session.request(
            method.upper(),
            url,
            params=params,
            data=data,
            timeout=cls.timeout,
        )
        try:
            response.raise_for_status()
            return response.json()["data"]
        except requests.exceptions.HTTPError as e:
            raise MCSMError(
                response.status_code, response.json().get("data", response.text)
            ) from e

    @classmethod
    async def upload(cls, url: str, file: bytes) -> bool:
        """上传文件"""

        response = cls.session.request(
            "POST",
            url,
            headers={"Content-Type": "multipart/form-data"},
            files={"file": file},
            timeout=cls.timeout,
        )
        try:
            response.raise_for_status()
            return True
        except requests.exceptions.HTTPError as e:
            raise MCSMError(
                response.status_code, response.json().get("data", response.text)
            ) from e


send = Request().send
upload = Request().upload

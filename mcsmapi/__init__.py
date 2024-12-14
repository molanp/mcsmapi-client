import urllib.parse
from .model import Overview
import requests
from .exceptions import crash_handler
from .APIs.APIPool import ApiPool
from .APIs.Users import Users


class MCSMAPI:
    def __init__(self, url, timeout=10):
        split_url = urllib.parse.urlsplit(url)
        self.mcsm_url = urllib.parse.urljoin(
            f"{split_url.scheme}://{split_url.netloc}", ""
        )
        self.apikey = None
        self.timeout = timeout
        self.token = None
        self.session = requests.Session()

    @crash_handler
    def __send(self, method, endpoint, params=None, data=None):
        if params is None:
            params = {}
        if not isinstance(endpoint, str):
            endpoint = str(endpoint)
        url = urllib.parse.urljoin(self.mcsm_url, endpoint)

        if self.apikey is not None:
            params["apikey"] = self.apikey
        if self.token is not None:
            params["token"] = self.token

        return self.session.request(
            method.upper(),
            url,
            params=params,
            data=data,
            timeout=self.timeout,
        ).json()["data"]

    def login(self, username, password):
        self.token = self.__send(
            "POST", ApiPool.LOGIN, data={"username": username, "password": password}
        )
        return self

    def login_with_apikey(self, apikey):
        self.apikey = apikey
        return self

    def overview(self):
        return Overview(self.__send("GET", ApiPool.OVERVIEW))
    
    def users(self):
        return Users(self.__send)

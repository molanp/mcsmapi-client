import urllib.parse
from .APIs.APIPool import ApiPool
from .APIs.Users import Users
from .model import Overview
from .request import Request, send

class MCSMAPI:
    def __init__(self, url, timeout):
        split_url = urllib.parse.urlsplit(url)
        Request.set_mcsm_url(urllib.parse.urljoin(
            f"{split_url.scheme}://{split_url.netloc}", ""
        ))
        self.authentication = None
        Request.set_timeout(timeout)

    def login(self, username, password):
        Request.set_token(send(
            "POST", ApiPool.LOGIN, data={"username": username, "password": password}
        ))
        self.authentication = "account"
        return self

    def login_with_apikey(self, apikey):
        Request.set_apikey(apikey)
        self.authentication = "apikey"
        return self

    def overview(self):
        return Overview(send("GET", ApiPool.OVERVIEW))

    def users(self):
        return Users()

    def daemon(self):
        return self.overview ().remoteList

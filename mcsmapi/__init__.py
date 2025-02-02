import urllib.parse
from mcsmapi.apis.daemon import Daemon
from mcsmapi.models.overview import OverviewModel
from mcsmapi.pool import ApiPool
from mcsmapi.apis.users import Users
from mcsmapi.apis.overview import Overview
from mcsmapi.request import Request, send


class MCSMAPI:
    def __init__(self, url, timeout) -> None:
        split_url = urllib.parse.urlsplit(url)
        Request.set_mcsm_url(
            urllib.parse.urljoin(f"{split_url.scheme}://{split_url.netloc}", "")
        )
        self.authentication = None
        Request.set_timeout(timeout)

    def login(self, username, password) -> "MCSMAPI":
        Request.set_token(
            send(
                "POST", ApiPool.LOGIN, data={"username": username, "password": password}
            )
        )
        self.authentication = "account"
        return self

    def login_with_apikey(self, apikey):
        Request.set_apikey(apikey)
        self.authentication = "apikey"
        return self

    def overview(self) -> OverviewModel:
        return Overview().init()

    def users(self) -> Users:
        return Users()

    def daemon(self) -> Daemon:
        return self.overview().remoteList

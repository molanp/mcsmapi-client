import urllib.parse
from mcsmapi.models.overview import OverviewModel
from mcsmapi.pool import ApiPool
from mcsmapi.apis.file import File
from mcsmapi.apis.user import User
from mcsmapi.apis.image import Image
from mcsmapi.apis.daemon import Daemon
from mcsmapi.apis.instance import Instance
from mcsmapi.apis.overview import Overview
from mcsmapi.request import Request


class MCSMAPI:
    def __init__(self, url: str, timeout: int = 5) -> None:
        split_url = urllib.parse.urlsplit(url)
        Request.set_mcsm_url(
            urllib.parse.urljoin(f"{split_url.scheme}://{split_url.netloc}", "")
        )
        self.authentication = None
        Request.set_timeout(timeout)

    def login(self, username: str, password: str) -> "MCSMAPI":
        Request.set_token(
            Request.send(
                "POST",
                f"{ApiPool.AUTH}/login",
                data={"username": username, "password": password},
            )
        )
        self.authentication = "account"
        return self

    def login_with_apikey(self, apikey: str):
        Request.set_apikey(apikey)
        self.authentication = "apikey"
        return self

    def overview(self) -> OverviewModel:
        return Overview().init()

    def instance(self) -> Instance:
        return Instance()

    def user(self) -> User:
        return User()

    def daemon(self) -> Daemon:
        return Daemon()

    def file(self) -> File:
        return File()

    def image(self) -> Image:
        return Image()

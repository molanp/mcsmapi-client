import requests


class ValidateError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ApiClient:
    def __init__(self, url, apikey=None, timeout=None):
        self.url = url
        self.apikey = apikey
        self.timeout = timeout
        self.cookies = None
        self.token = None

    def send(self, method, endpoint, params={}, data=None):
        url = f"{self.url}/api/{endpoint}"

        if self.apikey is not None:
            params["apikey"] = self.apikey
        if self.token is not None:
            params["token"] = self.token

        response = requests.request(
            method,
            url,
            params=params,
            json=data,
            cookies=self.cookies,
            timeout=self.timeout,
        )
        return response.json()


def support_login(cls):
    def login(self, username, password):
        seq = self.client.send(
            "POST", "auth/login", data={"username": username, "password": password}
        )
        if seq.status_code != 200:
            raise ValidateError(seq.json().get("data"))
        self.client.cookies = seq.cookies
        self.client.token = seq.json().get("data")

    setattr(cls, "login", login)
    return cls

from typing import List
from pydantic import BaseModel
from ..models.instance import UserInstancesList


class UserModel(BaseModel):
    uuid: str = ""
    userName: str = ""
    passWord: str = ""
    passWordType: int = 0
    salt: str = ""
    permission: int = 1  # 1=用户, 10=管理员, -1=被封禁的用户
    registerTime: str = ""
    loginTime: str = ""
    apiKey: str = ""
    isInit: bool = False
    secret: str = ""
    open2FA: bool = False
    instances: List["UserInstancesList"] = []



class SearchUserModel(BaseModel):
    total: int = 0
    page: int = 0
    page_size: int = 0
    max_page: int = 0
    data: List[UserModel] = []


from dataclasses import dataclass, field
from typing import List, Dict, cast
from mcsmapi.models.instance import UserInstancesList


@dataclass
class UserModel:
    uuid: str
    userName: str
    passWord: str
    passWordType: int
    salt: str
    permission: int  # 1=用户, 10=管理员, -1=被封禁的用户
    registerTime: str
    loginTime: str
    apiKey: str
    isInit: bool
    secret: str
    open2FA: bool
    instances: List[UserInstancesList] = field(default_factory=list)

    def __post_init__(self):
        # 如果 instances 是字典列表，则转换为 Instance 对象列表
        if isinstance(self.instances, list) and all(
            isinstance(instance, dict) for instance in self.instances
        ):
            self.instances = [
                UserInstancesList(
                    instanceUuid=cast(Dict[str, str], instance)["instanceUuid"],
                    daemonId=cast(Dict[str, str], instance)["daemonId"],
                )
                for instance in self.instances
            ]


@dataclass
class SearchUserModel:
    total: int
    page: int
    page_size: int
    max_page: int
    data: list = field(default_factory=list)

    def __post_init__(self):
        if isinstance(self.data, list) and all(
            isinstance(user, dict) for user in self.data
        ):
            self.data = [UserModel(**user) for user in self.data]

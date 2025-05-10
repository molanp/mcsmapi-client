from typing import Any, List
from pydantic import BaseModel
from mcsmapi.models.instance import InstanceDetail, UserInstancesList


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

    def delete(self) -> bool:
        """
        删除该用户。

        **返回:**
        - bool: 删除成功后返回True。
        """
        from mcsmapi.apis.user import User

        return User().delete([self.uuid])

    def update(self, config: dict[str, Any]) -> bool:
        """
        更新该用户的信息。

        参数:
        - config (dict[str, Any]): 用户的新信息，以字典形式提供，缺失内容使用原用户信息填充。

        返回:
        - bool: 更新成功后返回True。
        """
        from mcsmapi.apis.user import User

        updated_config = self.dict()
        updated_config.update(config)
        # 过滤用户信息中不需要的字段
        user_config_dict = {
            key: updated_config[key]
            for key in UserConfig.__fields__.keys()
            if key in updated_config
        }

        user_config = UserConfig(**user_config_dict).dict()

        return User().update(self.uuid, user_config)


class SearchUserModel(BaseModel):
    total: int = 0
    page: int = 0
    page_size: int = 0
    max_page: int = 0
    data: List[UserModel] = []


class UserConfig(BaseModel):
    uuid: str
    userName: str
    loginTime: str
    registerTime: str
    instances: List[InstanceDetail]
    permission: int  # 1=用户, 10=管理员, -1=被封禁的用户
    apiKey: str
    isInit: bool
    secret: str
    open2FA: bool

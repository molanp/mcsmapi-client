from enum import IntEnum
from typing import Any
from pydantic import BaseModel


class UserPermission(IntEnum):
    """用户权限级别"""

    BANNED = -1
    USER = 1
    ADMIN = 10


class UserInstances(BaseModel):
    """用户实例信息"""

    instanceUuid: str
    """实例UUID"""
    daemonId: str
    """节点ID"""


class UserCreateResult(BaseModel):
    """用户创建结果"""

    uuid: str
    """用户UUID"""
    userName: str
    """用户名"""
    permission: UserPermission
    """用户权限级别"""


class UserModel(BaseModel):
    """用户信息模型"""

    uuid: str = ""
    """用户UUID"""
    userName: str = ""
    """用户名"""
    loginTime: str = ""
    """最后登录时间 (YYYY/M/D hh:mm:ss)"""
    registerTime: str = ""
    """注册时间 (YYYY/M/D hh:mm:ss)"""
    instances: list[UserInstances] = []
    """用户拥有的实例列表"""
    permission: UserPermission = UserPermission.USER
    """用户权限级别"""
    passWord: str = ""
    """用户密码"""
    open2FA: bool = False
    """是否启用双因素认证 (2FA)"""
    apiKey: str = ""
    """用户 API 密钥"""
    passWordType: int = 1
    """密码类型 (已弃用)"""
    isInit: bool = False
    """是否为初始化用户 (已弃用)"""
    secret: str = ""
    """用户安全密钥 (已弃用)"""
    salt: str = ""
    """用户密码盐值 (已弃用)"""

    def delete(self):
        """
        删除该用户

        :returns: 操作成功后返回True
        """
        from mcsmapi.apis.user import User

        return User().delete([self.uuid])

    def update(self, config: dict[str, Any]):
        """
        更新该用户的信息

        :params config: 用户的新信息，以字典形式提供，缺失内容使用原用户信息填充

        :returns: 操作成功后返回True
        """
        from mcsmapi.apis.user import User

        user_config = self.model_dump()
        user_config.update(config)

        return User().update(self.uuid, user_config)


class SearchUserModel(BaseModel):
    """用户搜索结果"""

    total: int
    """匹配的用户总数"""
    page: int
    """当前页码"""
    page_size: int
    """每页返回的用户数量"""
    max_page: int
    """最大可用页数"""
    data: list[UserModel]
    """用户信息列表"""

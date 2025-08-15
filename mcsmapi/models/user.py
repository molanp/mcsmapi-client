from enum import IntEnum
from typing import Any
from pydantic import BaseModel
from mcsmapi.models.instance import InstanceDetail, UserInstancesList


class UserPermission(IntEnum):
    BANNED = -1
    USER = 1
    ADMIN = 10


class UserModel(BaseModel):
    """用户信息模型"""

    uuid: str = ""
    """用户唯一标识符 (UUID)"""
    userName: str = ""
    """用户名"""
    passWord: str = ""
    """用户密码 (存储加密后的字符串)"""
    passWordType: int = 0
    """密码类型 (0=默认类型)"""
    salt: str = ""
    """密码盐值 (用于加密)"""
    permission: UserPermission = UserPermission.USER
    """用户权限级别"""
    registerTime: str = ""
    """用户注册时间 (时间字符串格式)"""
    loginTime: str = ""
    """用户最后登录时间 (时间字符串格式)"""
    apiKey: str = ""
    """用户 API 密钥"""
    isInit: bool = False
    """是否为初始化用户 (系统内置用户)"""
    secret: str = ""
    """用户安全密钥 (可能用于额外的身份验证)"""
    open2FA: bool = False
    """是否启用双因素认证 (2FA)"""
    instances: list[UserInstancesList] = []
    """用户关联的实例列表"""

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

        updated_config = self.model_dump()
        updated_config.update(config)
        # 过滤用户信息中不需要的字段
        user_config_dict = {
            key: updated_config[key]
            for key in UserConfig.model_fields.keys()
            if key in updated_config
        }

        user_config = UserConfig(**user_config_dict).model_dump()

        return User().update(self.uuid, user_config)


class SearchUserModel(BaseModel):
    """用户搜索结果"""

    total: int = 0
    """匹配的用户总数"""
    page: int = 0
    """当前页码"""
    page_size: int = 0
    """每页返回的用户数量"""
    max_page: int = 0
    """最大可用页数"""
    data: list[UserModel] = []
    """用户信息列表"""


class UserConfig(BaseModel):
    """用户配置信息"""

    uuid: str
    """用户唯一标识符 (UUID)"""
    userName: str
    """用户名"""
    loginTime: str
    """最后登录时间"""
    registerTime: str
    """注册时间"""
    instances: list[InstanceDetail]
    """用户拥有的实例列表"""
    permission: UserPermission
    """用户权限级别"""
    apiKey: str
    """用户 API 密钥"""
    isInit: bool
    """是否为初始化用户 (系统内置用户)"""
    secret: str
    """用户安全密钥 (可能用于额外的身份验证)"""
    open2FA: bool
    """是否启用双因素认证 (2FA)"""

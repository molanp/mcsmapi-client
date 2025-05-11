from typing import Any, List
from pydantic import BaseModel
from mcsmapi.models.instance import InstanceDetail, UserInstancesList


class UserModel(BaseModel):
    """用户信息模型"""

    """用户唯一标识符 (UUID)"""
    uuid: str = ""
    """用户名"""
    userName: str = ""
    """用户密码 (存储加密后的字符串)"""
    passWord: str = ""
    """密码类型 (0=默认类型)"""
    passWordType: int = 0
    """密码盐值 (用于加密)"""
    salt: str = ""
    """用户权限级别 (1=用户, 10=管理员, -1=被封禁的用户)"""
    permission: int = 1
    """用户注册时间 (时间字符串格式)"""
    registerTime: str = ""
    """用户最后登录时间 (时间字符串格式)"""
    loginTime: str = ""
    """用户 API 密钥"""
    apiKey: str = ""
    """是否为初始化用户 (系统内置用户)"""
    isInit: bool = False
    """用户安全密钥 (可能用于额外的身份验证)"""
    secret: str = ""
    """是否启用双因素认证 (2FA)"""
    open2FA: bool = False
    """用户关联的实例列表"""
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
    """用户搜索结果"""

    """匹配的用户总数"""
    total: int = 0
    """当前页码"""
    page: int = 0
    """每页返回的用户数量"""
    page_size: int = 0
    """最大可用页数"""
    max_page: int = 0
    """用户信息列表"""
    data: List[UserModel] = []


class UserConfig(BaseModel):
    """用户配置信息"""

    """用户唯一标识符 (UUID)"""
    uuid: str
    """用户名"""
    userName: str
    """最后登录时间"""
    loginTime: str
    """注册时间"""
    registerTime: str
    """用户拥有的实例列表"""
    instances: List[InstanceDetail]
    """用户权限级别 (1=用户, 10=管理员, -1=被封禁的用户)"""
    permission: int
    """用户 API 密钥"""
    apiKey: str
    """是否为初始化用户 (系统内置用户)"""
    isInit: bool
    """用户安全密钥 (可能用于额外的身份验证)"""
    secret: str
    """是否启用双因素认证 (2FA)"""
    open2FA: bool

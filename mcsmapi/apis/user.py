from typing import Any, Literal
from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.user import SearchUserModel, UserConfig, UserCreateResult


class User:
    @staticmethod
    def search(
        username: str = "",
        page: int = 1,
        page_size: int = 20,
        role: Literal[-1, 1, 10, ""] = "",
    ) -> SearchUserModel:
        """
        根据用户名和角色搜索用户信息

        :params uername: 要搜索的用户名,为空则列出全部用户
        :params page: 页码，用于指示返回数据的第几页
        :params page_size: 每页数据条数
        :params role: 用于过滤的用户权限

        :returns: 包含搜索结果的模型
        """
        result = send(
            "GET",
            f"{ApiPool.AUTH}/search",
            params={
                "userName": username,
                "page": page,
                "pageSize": page_size,
                "role": role,
            },
        )
        return SearchUserModel(**result)

    @staticmethod
    def create(username: str, password: str, permission: int = 1) -> UserCreateResult:
        """
        创建新用户

        :params username: 用户名
        :params password: 密码
        :params permission: 权限等级

        :returns: 包含创建结果的模型
        """
        result = send(
            "POST",
            ApiPool.AUTH,
            data={"username": username, "password": password, "permission": permission},
        )
        return UserCreateResult(**result)

    @staticmethod
    def update(uuid: str, config: dict[str, Any]) -> bool:
        """
        更新用户信息

        **不建议直接使用此函数，建议调用search后使用用户对象的update方法按需更新**

        :params uuid: 用户的UUID
        :params config: 新的用户信息，以字典形式提供，缺失内容由 UserConfig 模型提供默认值

        :returns: 成功时返回True
        """
        return send(
            "PUT",
            ApiPool.AUTH,
            data={"uuid": uuid, "config": UserConfig(**config).model_dump()},
        )

    @staticmethod
    def delete(uuids: list[str]) -> bool:
        """
        删除用户

        :params uuids: 包含要删除的用户UUID的列表

        :returns: 成功时返回True
        """
        return send("DELETE", ApiPool.AUTH, data=uuids)

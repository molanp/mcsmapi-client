from typing import Any
from mcsmapi.pool import ApiPool
from mcsmapi.request import send
from mcsmapi.models.user import SearchUserModel, UserConfig


class User:
    def search(
        self, username: str = "", page: int = 1, page_size: int = 20, role: str = ""
    ) -> SearchUserModel:
        """根据用户名和角色搜索用户信息

        **参数:**
        - username (str): 要搜索的用户名。默认为空字符串，表示不进行用户名过滤
        - page (int): 页码，用于指示返回数据的页数。默认为1，表示返回第一页数据
        - page_size (int): 每页大小，用于指定每页包含的数据条数。默认为20，表示每页包含20条数据
        - role (str): 用户权限。默认为空字符串，表示不进行权限过滤
                     可用的值为 1=用户, 10=管理员, -1=被封禁的用户

        **返回:**
        - SearchUserModel: 包含搜索结果的模型。该模型包含了符合搜索条件的用户信息列表，以及总数据条数、总页数等分页信息。
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

    def create(self, username: str, password: str, permission: int = 1) -> str | bool:
        """
        创建新用户的方法

        **参数:**
        - username (str): 用户名，字符串类型
        - password (str): 密码，字符串类型
        - permission (int): 权限等级，整数类型，默认值为1

        **返回:**
        - str|bool: 创建成功后返回用户的UUID，如果未找到该字段，则默认返回True。
        """
        return send(
            "POST",
            ApiPool.AUTH,
            data={"username": username, "password": password, "permission": permission},
        ).get("uuid", True)

    def update(self, uuid: str, config: dict[str, Any]) -> bool:
        """
        更新用户信息的方法

        **不建议直接使用此函数，建议调用search后使用update方法按需更新**

        **参数:**
        - uuid (str): 用户的唯一标识符UUID
        - config (dict[str, Any]): 新的用户信息，以字典形式提供，缺失内容由UserConfig模型补全。

        **返回:**
        - bool: 成功时返回True
        """
        return send(
            "PUT",
            ApiPool.AUTH,
            data={"uuid": uuid, "config": UserConfig(**config).dict()},
        )

    def delete(self, uuids: list[str]) -> bool:
        """
        删除用户的方法

        **参数:**
        - uuids (list[str]): 包含要删除的用户UUID的列表。

        **返回:**
        - bool: 成功时返回True
        """
        return send("DELETE", ApiPool.AUTH, data=uuids)

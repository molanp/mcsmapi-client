from .APIPool import ApiPool


class Users:
    """管理 API 中与用户相关的操作

    提供通过 API 交互搜索、创建、更新和删除用户帐户的方法
    """

    def __init__(self, __send):
        self.__send = __send

    def search(self, username: str = "", page: int = 1, page_size: int = 20, role: str = "") -> dict:
        """根据用户名和角色搜索用户信息

        **参数:**
        - username (str): 要搜索的用户名。默认为空字符串，表示不进行用户名过滤
        - page (int): 页码，用于指示返回数据的页数。默认为1，表示返回第一页数据
        - page_size (int): 每页大小，用于指定每页包含的数据条数。默认为20，表示每页包含20条数据
        - role (str): 用户的角色。默认为空字符串，表示不进行角色过滤

        **
        - dict: 包含搜索结果的字典。该字典包含了符合搜索条件的用户信息列表，以及总数据条数、总页数等分页信息。
        """
        return self.__send("GET", ApiPool.USERS, params={"userName": username, "page": page, "pageSize": page_size, "role": role})

    def create(self, username: str, password: str, permission: int = 1) -> str | bool:
        """创建新用户的方法

        该方法接受用户名、密码和权限等级作为参数
        如果成功创建用户，将返回用户的唯一标识符UUID或True，这一行为由 MCSM 版本决定

        **参数:**
        - username (str): 用户名，字符串类型
        - password (str): 密码，字符串类型
        - permission (int): 权限等级，整数类型，默认值为1

        **返回:**
        - str|bool: 成功时返回用户UUID或True
        """
        return self.__send("POST", ApiPool.AUTH, data={"username": username, "password": password, "permission": permission}).get("uuid", True)

    def update(self, uuid: str, config: dict | None = None) -> bool:
        """更新用户信息的方法

        **如果需要更新用户非实例类配置，请先使用`search`获取对应用户的全部信息，然后根据需要修改对应的数据，作为`config`参数传入`update`方法**
        
        **更新用户的实例资源时，只传入对应的实例列表即可**

        **参数:**
        - `uuid` (str): 用户的唯一标识符UUID
        - `config` (dict | None): 配置字典，包含要更新的用户信息。默认为None

        **返回:**
        - `bool`: 成功时返回True
        """
        if config is None:
            config = {}
        return self.__send("PUT", ApiPool.AUTH, data={
            "uuid": uuid, "config": config})

    def delete(self, uuids: list | None = None) -> bool:
        """删除用户的方法

        **参数:**
        - `uuids` (list | None): 包含要删除的用户UUID的列表。默认为None

        **返回:**
        - `bool`: 成功时返回True
        """
        if uuids is None:
            uuids = []
        return self.__send("DELETE", ApiPool.AUTH, data=uuids)

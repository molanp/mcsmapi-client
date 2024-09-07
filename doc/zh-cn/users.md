# Users 类

`Users` 类表示一个与特定 API 端点进行交互以管理用户的客户端。

## 属性

- `client (ApiClient)`: 用于发送请求的 API 客户端。

## 初始化

`Users` 类在创建实例时会自动调用 `__init__` 方法进行初始化。

- **参数**:
  - `url (str)`: API 的基础 URL。
  - `apikey (str, optional)`: 用于身份验证的 API 密钥，默认值为 `None`。

## 方法

### `get_list`

```python
def get_list(self, username: str = "", page: int = 1, page_size: int = 10, role: str = "") -> requests.Response
```
**说明**: 从 API 获取用户列表。

- **参数**:

    - `username (str, optional)`: 要搜索的用户名，默认为空字符串。
    - `page (int, optional)`: 分页的页码，默认为 1。
    - `page_size (int, optional)`: 每页的项目数量，默认为 10。
    - `role (str, optional)`: 用于过滤的角色，默认为空字符串。
- **返回**:

    - `requests.Response`: 由 API 返回的用户列表。

### `create`
```python
def create(self, username: str, password: str, permission: int = 1) -> requests.Response
```
**说明**: 创建新用户。

- **参数**:

    - `username (str)`: 新用户的用户名。
    - `password (str)`: 新用户的密码。
    - `permission (int, optional)`: 新用户的权限级别，默认为 1。
- **返回**:

    - `requests.Response`: 创建用户后 API 返回的响应。

### `update`
```python
def update(self, uuid: str, config: dict = {}) -> requests.Response
```
**说明**: 更新现有用户。

- **参数**:

    - `uuid (str)`: 要更新的用户的 UUID。
    - `config (dict, optional)`: 用户的配置更新，默认为空字典。
- **返回**:

    - `requests.Response`: 更新用户后 API 返回的响应。

#### `delete`
```python
def delete(self, uuids: list = []) -> requests.Response
```
**说明**: 删除一个或多个用户。

- **参数**:

    - `uuids (list, optional)`: 要删除的用户的 UUID 列表，默认为空列表。
- **返回**:

    - `requests.Response`: 删除用户后 API 返回的响应。
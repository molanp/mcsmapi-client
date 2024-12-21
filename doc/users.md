# Users 类

管理API中与用户相关的操作。提供通过API交互搜索、创建、更新和删除用户帐户的方法。

## 初始化

```python
from mcsmapi import MCSMAPI

# 使用apikey登录(API权限取决于apikey权限)
mcsm = MCSMAPI("https://example.com").login_with_apikey("apikey")

users_manager = mcsm.users()
```

## 方法

### search

根据用户名和角色搜索用户信息。

**参数:**
- `username` (str): 要搜索的用户名。默认为空字符串，表示不进行用户名过滤。
- `page` (int): 页码，用于指示返回数据的页数。默认为1，表示返回第一页数据。
- `page_size` (int): 每页大小，用于指定每页包含的数据条数。默认为20，表示每页包含20条数据。
- `role` (str): 用户的角色。默认为空字符串，表示不进行角色过滤。

**返回:**
- `dict`: 包含搜索结果的字典。该字典包含了符合搜索条件的用户信息列表，以及总数据条数、总页数等分页信息。

**代码示例:**
```python
users_manager.search()
```

### create

创建新用户的方法。该方法接受用户名、密码和权限等级作为参数。如果成功创建用户，将返回用户的唯一标识符UUID或True，这一行为由MCSM版本决定。

**参数:**
- `username` (str): 用户名，字符串类型。
- `password` (str): 密码，字符串类型。
- `permission` (int): 权限等级，整数类型，默认值为1。

**返回:**
- `str|bool`: 成功时返回用户UUID或True

**代码示例:**
```python
users_manager.create("username", "password")
```

### update

更新用户信息的方法。

> [!Important]
> 如果需要更新用户非实例类配置，请先使用`search`获取对应用户的全部信息，然后根据需要修改对应的数据，作为`config`参数传入`update`方法。
>
> 更新用户的实例资源时，只传入对应的实例列表即可

**参数:**
- `uuid` (str): 用户的唯一标识符UUID。
- `config` (dict | None): 配置字典，包含要更新的用户信息。默认为None。

**返回:**
- `bool`: 成功时返回True

**代码示例:**
```python
users_manager.update("b7b5bc87eb454b52bbccc7f6c99dc333")
```

### delete

删除用户的方法。

**参数:**
- `uuids` (list | None): 包含要删除的用户UUID的列表。默认为None。

**返回:**
- `bool`: 成功时返回True

**代码示例:**
```python
users_manager.delete(["b7b5bc87eb454b52bbccc7f6c99dc333"])
```

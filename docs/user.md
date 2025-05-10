# [User](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/user.py)

[example/user](https://github.com/molanp/mcsmapi/blob/main/example/user.py)

该模块提供对用户账户的管理接口，包括搜索、创建、更新和删除用户等操作。

---

### [search(username="", page=1, page_size=20, role="")](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/user.py#L7-L32)

#### 功能

根据用户名和角色搜索用户信息。

#### 参数说明：

| 参数名    | 类型 | 默认值 | 描述                                                                |
| --------- | ---- | ------ | ------------------------------------------------------------------- |
| username  | str  | ""     | 用户名关键字，模糊匹配                                              |
| page      | int  | 1      | 当前页码                                                            |
| page_size | int  | 20     | 每页数据量                                                          |
| role      | str  | ""     | 角色筛选。可用值: `"1"`(普通用户), `"10"`(管理员), `"-1"`(封禁用户) |

#### 返回值：

- [SearchUserModel](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/models/user.py) 对象，包含以下字段：
  - `.data`: 用户列表
  - `.total`: 总记录数
  - `.page`: 当前页码
  - `.pageSize`: 每页大小

#### 示例：

```python
users = api.user().search(role="10")  # 查找所有管理员
for user in users.data:
    print(user.userName)
```

---

### [create(username, password, permission=1)](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/user.py#L34-L50)

#### 功能

创建新用户。

#### 参数说明：

| 参数名     | 类型 | 必填 | 描述                             |
| ---------- | ---- | ---- | -------------------------------- |
| username   | str  | 是   | 用户名                           |
| password   | str  | 是   | 密码                             |
| permission | int  | 否   | 权限等级，默认为 `1`（普通用户） |

#### 返回值：

- 成功时返回用户的 `uuid`字符串，旧版本可能返回 `True`

#### 示例：

```python
uuid = api.user().create("new_user", "password123")
print("Created user uuid:", uuid)
```

---

### [update(uuid, config)](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/user.py#L52-L69)

#### 功能

更新指定用户的信息。

⚠️ **注意**：建议先通过 [search()](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/user.py#L7-L32) 获取用户对象后调用其 [update()](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/user.py#L52-L69) 方法。

#### 参数说明：

| 参数名 | 类型           | 必填 | 描述                                    |
| ------ | -------------- | ---- | --------------------------------------- |
| uuid   | str            | 是   | 用户唯一标识符                          |
| config | dict[str, Any] | 是   | 要更新的配置项，如 `{"permission": -1}` |

#### 返回值：

- 成功时返回 `True`

#### 示例：

```python
api.user().update("some-uuid-here", {"permission": -1})  # 封禁用户
```

---

### [delete(uuids)](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/user.py#L71-L81)

#### 功能

批量删除用户。

#### 参数说明：

| 参数名 | 类型      | 必填 | 描述           |
| ------ | --------- | ---- | -------------- |
| uuids  | list[str] | 是   | 用户 UUID 列表 |

#### 返回值：

- 成功时返回 `True`

#### 示例：

```python
api.user().delete(["uuid1", "uuid2"])  # 删除两个用户
```

---

## 基本使用示例

### 初始化 SDK 并登录

```python
from mcsmapi import MCSMAPI

api = MCSMAPI("http://localhost:23333")
api.login("admin", "your_password_here")
```

### 查询所有用户并输出用户名

```python
userManager = api.user()
users = userManager.search()

for user in users.data:
    print(user.userName)
```

### 创建一个用户并删除

```python
uuid = userManager.create("test_user", "secure_password")
if isinstance(uuid, str):
    userManager.delete([uuid])
else:
    found = userManager.search(username="test_user").data[0]
    found.delete()
```

### 更新用户权限（封禁用户）

```python
user = userManager.search(username="test_user").data[0]
user.update({"permission": -1})
```

---

## 注意事项

- [create()](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/user.py#L34-L50) 的返回值类型可能因版本不同而异，需做兼容性判断。
- 不建议直接使用 [update(uuid, config)](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/user.py#L52-L69)，推荐通过 [search()](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/user.py#L7-L32) 获取用户对象后再调用 [update()](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/user.py#L52-L69) 方法。

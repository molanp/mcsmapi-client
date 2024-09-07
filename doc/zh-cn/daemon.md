# Daemon 类

`Daemon` 类表示一个与特定守护进程服务进行交互的客户端。

## 属性

- `client (ApiClient)`: 用于发送请求的 API 客户端。

## 初始化

`Daemon` 类在创建实例时会自动调用 `__init__` 方法进行初始化。

- **参数**:
  - `url (str)`: 守护进程服务的基础 URL。
  - `apikey (str, optional)`: 用于身份验证的 API 密钥，默认值为 `None`。

## 方法

### `getList`

```python
def getList(self) -> list
```
**说明**: 获取远程服务列表。

- **返回**:
    - `list`: 远程服务列表。

### `add`
```python
def add(self, ip: str, port: int, remarks: str, apiKey: str, prefix: str = "") -> requests.Response
```
**说明**: 添加新的远程服务。

- **参数**:

    - `ip (str)`: 远程服务的 IP 地址。
    - `port (int)`: 远程服务的端口号。
    - `remarks (str)`: 远程服务的备注或描述。
    - `apiKey (str)`: 远程服务的 API 密钥。
    - `prefix (str, optional)`: 远程服务的可选前缀，默认为空字符串。
- **返回**:

    - `requests.Response`: 服务器返回的响应数据。

### `delete`
```python
def delete(self, uuid: str) -> requests.Response
```
**说明**: 根据 UUID 删除远程服务。

- **参数**:

    - `uuid (str)`: 要删除的远程服务的 UUID。
- **返回**:

    - `requests.Response`: 服务器返回的响应数据。

### `tryConnect`
```python
def tryConnect(self, uuid: str, return_bool: bool = False) -> requests.Response || bool
```
**说明**: 尝试连接到指定 UUID 的远程服务。

- **参数**:

    - `uuid (str)`: 要连接的远程服务的 UUID。
    - `return_bool (bool)`: 是否只返回连接状态布尔值，默认为 `False`。
- **返回**:

    - `requests.Response || bool`: 服务器返回的响应数据或节点可以状态的布尔值

### `updateDaemonConnectConfig`
```python
def updateDaemonConnectConfig(self, uuid: str, ip: str, port: int, remarks: str, apiKey: str, available: bool = False, prefix: str = "") -> requests.Response
```
**说明**: 更新远程服务的配置。

- **参数**:

    - `uuid (str)`: 要更新的远程服务的 UUID。
    - `ip (str)`: 新的 IP 地址。
    - `port (int)`: 新的端口号。
    - `remarks (str)`: 新的备注或描述。
    - `apiKey (str)`: 新的 API 密钥。
    - `available (bool, optional)`: 服务是否可用，默认为 `False。`
    - `prefix (str, optional):` 可选的前缀，默认为空字符串。
- **返回**:

    - `requests.Response`: 服务器返回的响应数据。
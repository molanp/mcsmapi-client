# [Overview](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/overview.py#L6-L23) 模块文档

[example/overview](https://github.com/molanp/mcsmapi/blob/main/example/overview.py)

位于：`mcsmapi/apis/overview.py`

该模块用于获取系统概览信息，包括版本、系统资源、运行状态、图表数据以及远程守护进程等信息。

## 类：[Overview](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/overview.py#L6-L23)

通过 `MCSMAPI().overview()` 获取 [Overview](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/overview.py#L6-L23) 实例。

---

### 方法一：[init()](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/apis/overview.py#L10-L23)

#### 功能

**内部方法，请勿直接调用**

初始化方法，用于获取 API 概览信息并构建 [OverviewModel](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/models/overview.py#L57-L98) 实例。

#### 参数说明：

无参数。

#### 返回值：

- [OverviewModel](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/models/overview.py#L57-L98) 对象，包含以下字段：

| 字段名                 | 类型                                                                                              | 描述                             |
| ---------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------- |
| version                | str                                                                                               | 当前服务端版本号                 |
| specifiedDaemonVersion | str                                                                                               | 指定使用的 Daemon 版本           |
| system                 | [SystemInfo](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/models/overview.py#L14-L36)      | 系统信息（内存、负载、主机名等） |
| record                 | [RecordInfo](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/models/overview.py#L38-L45)      | 登录记录统计信息                 |
| process                | [ProcessInfo](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/models/overview.py#L47-L53)     | 进程资源占用情况（CPU、内存）    |
| chart                  | [ChartInfo](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/models/overview.py#L55-L64)       | 图表数据（系统和请求趋势）       |
| remoteCount            | [RemoteCountInfo](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/models/overview.py#L66-L71) | 远程守护进程数量统计             |
| remote                 | List[[DaemonModel](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/models/daemon.py)]                           | 所有远程守护进程列表             |

#### 示例：

```python
overview = api.overview()
print("当前服务端版本:", overview.version)
```

---

## 基本使用示例

### 初始化 SDK 并登录

```python
from mcsmapi import MCSMAPI

api = MCSMAPI("http://localhost:23333")
api.login("admin", "your_password_here")  
# 或使用 login_with_apikey
# api.login_with_apikey("your_apikey_here")
```

### 获取系统概览信息

```python
overview = api.overview()

print("服务端版本:", overview.version)
print("系统内存剩余:", overview.system.freemem)
print("系统负载平均值:", overview.system.loadavg)
print("MC-SMA 运行 CPU 占用率:", overview.process.cpu)
```

### 遍历所有远程守护进程

```python
for remote in overview.remote:
    print("备注名称:", remote.remarks)
    print("IP 地址:", remote.ip)
    print("端口号:", remote.port)
    print("路径前缀:", remote.prefix)
    print("是否可用:", remote.available)
    print("守护进程版本:", remote.version)
    print("守护进程 CPU 占用率:", remote.process.cpu)
    print("系统主机名:", remote.system.hostname)
    print("系统剩余内存:", remote.system.freemem)
```

### 连接并操作远程守护进程

```python
remote = overview.remote[0]

remote.link()  # 连接到远程守护进程

# 删除远程实例
remote.deleteInstance(["uuid1", "uuid2"], True)

# 更新守护进程配置
remote.updateConfig({"prefix": "", "remarks": "新的备注名"})

# 删除该守护进程
remote.delete()
```

---

## 数据模型详解

### SystemInfo

表示本地服务器或远程守护进程的系统信息。

| 字段名   | 类型                                                                                        | 描述                            |
| -------- | ------------------------------------------------------------------------------------------- | ------------------------------- |
| user     | [SystemUser](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/models/overview.py#L5-L12) | 当前运行用户信息                |
| time     | int                                                                                         | 当前时间戳                      |
| totalmem | int                                                                                         | 总内存大小（字节）              |
| freemem  | int                                                                                         | 可用内存大小（字节）            |
| type     | str                                                                                         | 系统类型（如 Linux）            |
| version  | str                                                                                         | 内核版本                        |
| node     | str                                                                                         | 节点名称                        |
| hostname | str                                                                                         | 主机名                          |
| loadavg  | list[float]                                                                                 | 系统负载平均值（1, 5, 15 分钟） |
| platform | str                                                                                         | 操作系统平台                    |
| release  | str                                                                                         | 操作系统发行版                  |
| uptime   | float                                                                                       | 系统运行时长（秒）              |
| cpu      | float                                                                                       | CPU 使用率（百分比）            |

### ProcessInfo

表示 MC-SMA 服务或远程守护进程的资源使用情况。

| 字段名 | 类型 | 描述                 |
| ------ | ---- | -------------------- |
| cpu    | int  | CPU 使用率（百分比） |
| memory | int  | 内存使用量（MB）     |
| cwd    | str  | 当前工作目录         |

### RemoteCountInfo

表示远程守护进程的数量统计。

| 字段名    | 类型 | 描述     |
| --------- | ---- | -------- |
| total     | int  | 总数     |
| available | int  | 可用数量 |

### DaemonModel (远程守护进程模型)

继承自 [SystemInfo](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/models/overview.py#L14-L36)，新增如下字段：

| 字段名    | 类型 | 描述               |
| --------- | ---- | ------------------ |
| ip        | str  | 守护进程 IP 地址   |
| port      | int  | 守护进程端口       |
| prefix    | str  | 请求路径前缀       |
| remarks   | str  | 备注名称           |
| available | bool | 是否可用           |
| version   | str  | 守护进程版本       |
| uuid      | str  | 守护进程唯一标识符 |

---

## 注意事项

- 请确保已成功调用 `login()` 或 `login_with_apikey()` 后再执行 `overview()`。
- [remote](https://github.com/molanp/mcsmapi/blob/main/example/overview.py#L28-L28) 列表中的每个对象都支持 `.link()`、`.deleteInstance()`、`.updateConfig()` 和 `.delete()` 等操作，请谨慎使用。
- [updateConfig()](https://github.com/molanp/mcsmapi/blob/main/mcsmapi/models/daemon.py#L72-L95) 中传入的参数为 dict 类型，仅需提供需要修改的字段即可。

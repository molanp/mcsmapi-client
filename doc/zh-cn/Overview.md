# Overview 类

表示系统概览信息的类。

**属性:**
- `version` (str): MCSM版本。
- `specifiedDaemonVersion` (str): 指定的守护进程版本。
- `system` (SystemInfo): 系统信息对象。
- `record` (RecordInfo): 记录信息对象。
- `process` (ProcessInfo): 进程信息对象。
- `chart` (dict): 图表信息。
- `remoteCount` (RemoteCountInfo): 远程连接数量。
- `remoteList` ([Daemon](Daemon.md)): 远程连接列表对象，由`Daemon`类初始化。


## SystemInfo 类

表示面板系统信息的类。

**属性:**
- `type` (str): 系统类型。
- `version` (str): 系统版本。
- `platform` (str): 系统平台。

## RecordInfo 类

表示面板记录信息的类。

**属性:**
- `logined` (int): 面板登录成功次数
- `loginFailed` (int): 登录失败次数
- `banips` (int): 临时封禁IP数
- `illegalAccess` (int): 已阻止的访问数

## ProcessInfo 类

表示面板进程信息的类。

**属性:**
- `cpu` (int): CPU使用率。
- `memory` (int): 内存使用率。
- `cwd` (str): 当前工作目录。

## RemoteCountInfo 类

表示面板远程连接数量的类。

**属性:**
- `available` (int): 在线数量
- `total` (int): 总数量

## 代码示例
```python
from mcsmapi import MCSMAPI

mcsm = MCSMAPI("https://example.com").login_with_apikey("apikey")
# 初始化 Overview 类
overview = mcsm.overview()

# 获取 MCSM 版本
mcsm_version = mcsm.overview().mcsm_version

# 获取平台架构
platform = mcsm.overview().system.platform
```

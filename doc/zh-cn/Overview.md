# Overview 类

表示系统概览信息的类。

**属性:**
- `version` (str): MCSM版本。
- `specifiedDaemonVersion` (str): 指定的守护进程版本。
- `system` (SystemInfo): 系统信息对象，由 `SystemInfo` 类实例化。
- `record` (dict): 记录信息。
    - `logined` (int): 面板登录成功次数
    - `loginFailed` (int): 登录失败次数
    - `banips` (int): 临时封禁IP数
    - `illegalAccess` (int): 已阻止的访问数
- `process` (dict): 进程信息。
    - `cpu` (int): CPU使用率。
    - `memory` (int): 内存使用率。
    - `cwd` (str): 当前工作目录。
- `chart` (dict): 图表信息。
- `remoteCount` (dict): 远程连接在线数量和总数量。
    - `available` (int): 在线数量
    - `total` (int): 总数量
- `remoteList` ([Daemon](Daemon.md)): 远程连接列表对象，由`Daemon`类初始化。


# SystemInfo 类

表示系统信息的类。

**参数:**
- `system_data` (dict): 包含系统信息的字典。

**属性:**
- `type` (str): 系统类型。
- `version` (str): 系统版本。
- `platform` (str): 系统平台。


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
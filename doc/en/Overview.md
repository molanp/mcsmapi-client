# Overview class Class

representing system overview information.

**Attributes:**

- `version` (str): MCSM version.
- `specifiedDaemonVersion` (str): Specified daemon version.
- `system` (SystemInfo): System information object.
- `record` (RecordInfo): Record information object.
- `process` (ProcessInfo): Process information object.
- `chart` (dict): Chart information.
- `remoteCount` (RemoteCountInfo): Number of remote connections.
- `remoteList` (Daemon): Remote connection list object, initialized by `Daemon` class.

## The SystemInfo class

represents the panel system information.

**Properties:**

- `type` (str): System type.
- `version` (str): System version.
- `platform` (str): System platform.

## The RecordInfo class

represents the panel record information.

**Properties:**

- `logined` (int): Number of successful panel logins.
- `loginFailed` (int): Number of failed login attempts.
- `banips` (list): List of IPs to temporarily block.
- `illegalAccess` (int): Number of blocked accesses.

## The ProcessInfo class

represents the panel process information.

**Properties:**

- `cpuUsage` (float): CPU utilization.
- `memoryUsage` (float): Memory usage.
- `cwd` (str): Current working directory.

## The RemoteCountInfo class

represents the number of remote connections to the panel.

**Properties:**

- `total` (int): Total number.
- `available` (int): Number of online connections.

# Code example

```python
from mcsmapi import MCSMAPI

mcsm = MCSMAPI("https://example.com:23333").login_with_apikey("your_apikey")

# Initialize Overview class overview = mcsm.overview()
overview = mcsm.overview()

# Get MCSM version
mcsm_version = overview.version#

# Get platform architecture
platform = overview.system.platform
```

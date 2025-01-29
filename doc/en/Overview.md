# Overview Class

Class representing system overview information.

**Attributes:**
- `version` (str): MCSM version.
- `specifiedDaemonVersion` (str): Specified daemon version.
- `system` (SystemInfo): System information object.
- `record` (RecordInfo): Record information object.
- `process` (ProcessInfo): Process information object.
- `chart` (dict): Chart information.
- `remoteCount` (RemoteCountInfo): Number of remote connections.
- `remoteList` ([Daemon](Daemon.md)): Remote connection list object, initialized by `Daemon` class.


## SystemInfo Class

Class representing panel system information.

**Properties:**
- `type` (str): System type.
- `version` (str): System version.
- `platform` (str): System platform.

## RecordInfo Class

Class for panel record information.

**Properties:**
- `logined` (int): The number of successful panel logins.
- `loginFailed` (int): Number of failed login attempts.
- `banips` (int): Number of IPs temporarily blocked.
- `illegalAccess` (int): Number of blocked accesses

## ProcessInfo Class

Class representing information about the panel's processes.

**Properties:**
- `cpu` (int): CPU utilization.
- `memory` (int): Memory utilization.
- `cwd` (str): Current working directory.

## RemoteCountInfo class

Class representing the number of remote connections to the panel.

**Attributes:**
- `available` (int): Number of online connections.
- `total` (int): Total number of connections.

## Code example
``python
from mcsmapi import MCSMAPI

mcsm = MCSMAPI(“https://example.com”).login_with_apikey(“apikey”)
# Initialize the Overview class
overview = mcsm.overview()

# Get the MCSM version
mcsm_version = mcsm.overview().mcsm_version

# Get the platform architecture
platform = mcsm.overview().system.platform
``

# `Overview` Class

Represents system overview information.

### **Attributes:**
- `version` (str): MCSM version.
- `specifiedDaemonVersion` (str): The specified daemon version.
- `system` (SystemInfo): A system information object, instantiated by the `SystemInfo` class.
- `record` (dict): Log records.
  - `logined` (int): Number of successful logins to the panel.
  - `loginFailed` (int): Number of failed login attempts.
  - `banips` (int): Number of temporarily banned IP addresses.
  - `illegalAccess` (int): Number of blocked illegal access attempts.
- `process` (dict): Process information.
  - `cpu` (int): CPU usage percentage.
  - `memory` (int): Memory usage percentage.
  - `cwd` (str): Current working directory.
- `chart` (dict): Chart data.
- `remoteCount` (dict): Remote connection count, both online and total.
  - `available` (int): Number of online connections.
  - `total` (int): Total number of connections.
- `remoteList` (list): List of remote connections.

---

# `SystemInfo` Class

Represents system information.

### **Parameters:**
- `system_data` (dict): A dictionary containing system information.

### **Attributes:**
- `type` (str): The type of the system.
- `version` (str): The version of the system.
- `platform` (str): The platform of the system.

---

## Code Example
```python
from mcsmapi import MCSMAPI

# Initialize MCSM API client and log in with API key
mcsm = MCSMAPI("https://example.com").login_with_apikey("apikey")

# Initialize Overview class
overview = mcsm.overview()

# Get MCSM version
mcsm_version = mcsm.overview().mcsm_version

# Get platform architecture
platform = mcsm.overview().system.platform
```

### **Explanation:**
- The `Overview` class provides various system-related details, such as MCSM version, daemon version, system stats (like CPU and memory usage), remote connection stats, and more.
- The `SystemInfo` class gives you detailed information about the system, such as the type, version, and platform.
- In the provided example, the `mcsmapi` library is used to connect to a server and fetch overview information, including the version of MCSM and system platform architecture.

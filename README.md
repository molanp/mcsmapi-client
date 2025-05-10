# MCSM API

![Supported MCSManager Versions](https://img.shields.io/badge/Supported%20MCSManager%20Versions-10.x-blue)
![Python Version](https://img.shields.io/badge/Python%20Version-%3E%3D3.7-blue)
![PyPI Downloads](https://img.shields.io/pypi/dm/mcsmapi)

English|[Chinese Simplified](README_zh-cn.md)

> [!important]
> We need your help, the documentation for this project has not been written yet, if you are willing, please submit pr to help us write the documentation.

## Documentation

The documentation is not yet complete, if you need it, please visit [https://deepwiki.com/molanp/mcsmapi](https://deepwiki.com/molanp/mcsmapi)

## Introduction

`mcsmapi` is a PyPI package based on [MCSManager](https://github.com/MCSManager/MCSManager), designed to simplify interactions with the MCSM API.

With this library, you can more easily access and operate the various features provided by MCSM.

## Installation

You can install `mcsmapi` using `pip`:

```bash
pip install mcsmapi
```

## Supported Features

- [x] Dashboard data (`Overview`)
- [x] User management (`User`)
- [x] Instance management (`Instance`)
- [x] Daemon management (`Daemon`)
- [x] File management (`File`)
- [x] Image management (`Image`)

## Supported MCSM Versions

| MCSM Version | Support Status |
| :---: | :---: |
| 10.x | ✅ |

### Quick Example

```python
from mcsmapi import MCSMAPI

# Initialize
mcsm = MCSMAPI("https://example.com") # https or http required

# Log in with username and password (API permissions depend on the account permissions)
mcsm.login("username", "password")

# Log in with API key (API permissions depend on the API key permissions)
mcsm.login_with_apikey("apikey")

# Get dashboard data
overview = mcsm.overview()

# Get MCSM version
mcsm_version = mcsm.overview().version
```

## Contributing

If you encounter any issues or have suggestions for improvements, feel free to submit an [Issue](https://github.com/molanp/mcsmapi/issues) or create a [Pull Request](https://github.com/molanp/mcsmapi/pulls).

## License

`mcsmapi` is licensed under the [MIT License](https://opensource.org/licenses/MIT).

Please refer to the [LICENSE](LICENSE) file for more details.

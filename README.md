# MCSM API Client

![Supported MCSManager Versions](https://img.shields.io/badge/Supported%20MCSManager%20Versions-10.2.1,10.1.0-blue)
![Python Version](https://img.shields.io/badge/Python%20Version-%3E%3D3.7-blue)
![PyPI Downloads](https://img.shields.io/pypi/dm/mcsmapi)

English|[简体中文](README_zh-cn.md)

## Introduction

`mcsmapi` is a Pypi package based on [MCSManager](https://github.com/MCSManager/MCSManager), designed to simplify interaction with MCSM API.

Through this library, you can easily access and operate various functions provided by MCSM.

## Installation

You can use `pip` to install `mcsmapi`:

```bash
pip install mcsmapi
```

## Usage method

### Example code

Here are some examples of how to use `mcsmapi`:

```python
from mcsmapi import overview

# if you have a apikey, you can use this method
client = Overview(url=" https://example.com/",apikey="your_api_key")

# if you do not have a apikey, you can use this method
client = Overview(url=" https://example.com/")
# login
client.login(username="your_username",password="your_password")

# Get dashboard data
response = client.getData()
print(response.json())
```

### Supported functions

- [x] Login (`(func) login`)
- [x] Dashboard Data (`(cls) Overview`)
- [x] User Management (`(cls) Users`)
- [x] Instance Management (`(cls) Instance`)
- [x] Daemon Management (`(cls) Daemon`)
- [x] File Management (`(cls) File`)
- [x] Image Management (`(cls) Image`)

## Supported MCSM versions

The current version of MCSMAPI client supports the following MCSM versions:

- 10.2.1
- 10.1.0

## Compatible Python versions

- Python version 3.7 and above.

## Contribution

If you find any issues or have improvement suggestions, please feel free to submit [Issue](https://github.com/molanp/mcsmapi-client/issues) or create a [Pull Request](https://github.com/molanp/mcsmapi-client/pulls).

## License

[MIT License](https://opensource.org/licenses/MIT).

Please refer to [LICENSE](LICENSE) File for more information.

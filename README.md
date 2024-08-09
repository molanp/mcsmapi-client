# MCSM API Client

![Supported MCSManager Versions](https://img.shields.io/badge/Supported%20MCSManager%20Versions-10.2.1,10.1.0-blue)
![Python Version](https://img.shields.io/badge/Python%20Version-%3E%3D3.7-blue)
![PyPI Downloads](https://img.shields.io/pypi/dm/mcsmapi-client)

English|[简体中文](README_zh-cn.md)

## Introduction

`mcsmapi-client` is a Pypi package based on [MCSManager](https://github.com/MCSManager/MCSManager), designed to simplify interaction with MCSM API.

Through this library, you can easily access and operate various functions provided by MCSM.

## Installation

You can use `pip` to install `mcsmapi-client`:

```bash
pip install mcsmapi-client
```

## Usage method

### Example code

Here are some examples of how to use `mcsmapi-client`:

```python
from mcsmapi_client import Overview

# Create a panel API client instance
client = Overview(url=" https://example.com/",apikey="your_api_key")


response = client.get_data()
print(response)
```

### Supported functions

- [x] Dashboard Data (`Overview`)
- [x] User Management (`Users`)
- [x] Instance Management (`Instance`)
- [ ] Node Management (``)
- [ ] File Management (``)
- [ ] Image Management (``)

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

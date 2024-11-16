# MCSM API Client

![Supported MCSManager Versions](https://img.shields.io/badge/Supported%20MCSManager%20Versions-10.2.1,10.1.0-blue)
![Python Version](https://img.shields.io/badge/Python%20Version-%3E%3D3.7-blue)
![PyPI Downloads](https://img.shields.io/pypi/dm/mcsmapi)

Simplified Chinese|[English](https://github.com/molanp/mcsmapi/blob/main/README.md)

## Introduction

`mcsmapi` is a Pypi package based on [MCSManager](https://github.com/MCSManager/MCSManager) designed to simplify interaction with the MCSM API.

With this library, you can more easily access and manipulate the various features provided by MCSM.

## Installation

You can install `mcsmapi` using `pip`:

```bash
pip install mcsmapi
```

## Supported functions

- [x] login ([login](/doc/en/login.md))
- [x] Dashboard data ([Overview](/doc/en/overview.md))
- [x] User Management ([Users](/doc/en/users.md))
- [x] Instance Management (`Instance`)
- [x] Node Management ([Daemon](/doc/en/daemon.md))
- [x] File Management (`File`)
- [x] Image Management (`Image`)

## Supported MCSM versions

| MCSM Version | Support Status | Compatible Versions|
|:---:| :---: | :---: |
| 10.1.0 ~ 10.4.2 | ✅ | 0.1.1 |

## Contribute

If you find any issues or have suggestions for improvements, feel free to submit an [Issue](https://github.com/molanp/mcsmapi/issues) or create a [Pull Request](https://github.com/molanp/mcsmapi/pulls).

## License

`mcsmapi` uses the [MIT license](https://opensource.org/licenses/MIT).

See the [LICENSE](LICENSE) file for more information.
# MCSM API Client

![Supported MCSManager Versions](https://img.shields.io/badge/Supported%20MCSManager%20Versions-10.2.1,10.1.0-blue)
![Python Version](https://img.shields.io/badge/Python%20Version-%3E%3D3.7-blue)
![PyPI Downloads](https://img.shields.io/pypi/dm/mcsmapi)

简体中文|[English](https://github.com/molanp/mcsmapi/blob/main/README.md)

## 简介

`mcsmapi` 是一个基于 [MCSManager](https://github.com/MCSManager/MCSManager) 的 Pypi包，旨在简化与MCSM API的交互。

通过这个库，您可以更轻松地访问和操作MCSM提供的各种功能。

## 安装

您可以使用 `pip` 安装 `mcsmapi`：

```bash
pip install mcsmapi
```

## 支持的功能

- [x] 登录 ([login](doc/zh-cn/login.md))
- [x] 仪表盘数据([Overview](/doc/zh-cn/overview.md))
- [x] 用户管理([Users](doc/zh-cn/users.md))
- [x] 实例管理(`Instance`)
- [x] 节点管理([Daemon](doc/zh-cn/daemon.md))
- [x] 文件管理(`File`)
- [x] 镜像管理(`Image`)

## 支持的 MCSM 版本

| MCSM 版本 | 支持状态 | 兼容版本 |
| :---: | :---: | :---: |
| 10.1.0 - 10.2.1 | ✅ | 0.1.1 |

## 贡献

如果您发现任何问题或有改进建议，欢迎提交 [Issue](https://github.com/molanp/mcsmapi/issues) 或者创建 [Pull Request](https://github.com/molanp/mcsmapi/pulls)。

## 许可

`mcsmapi` 使用 [MIT 许可证](https://opensource.org/licenses/MIT)。

请参阅 [LICENSE](LICENSE) 文件以获取更多信息。

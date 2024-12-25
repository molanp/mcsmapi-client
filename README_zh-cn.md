# MCSM API

![Supported MCSManager Versions](https://img.shields.io/badge/Supported%20MCSManager%20Versions-10.x-blue)
![Python Version](https://img.shields.io/badge/Python%20Version-%3E%3D3.7-blue)
![PyPI Downloads](https://img.shields.io/pypi/dm/mcsmapi)

简体中文|[English](README.md)

## 简介

`mcsmapi` 是一个基于 [MCSManager](https://github.com/MCSManager/MCSManager) 的 Pypi包，旨在简化与MCSM API的交互。

通过这个库，您可以更轻松地访问和操作MCSM提供的各种功能。

## 安装

您可以使用 `pip` 安装 `mcsmapi`：

```bash
pip install mcsmapi
```

## 支持的功能

- [x] 仪表盘数据([Overview](doc/zh-cn/overview.md))
- [x] 用户管理([Users](doc/zh-cn/users.md))
- [ ] 实例管理(`Instance`)
- [ ] 节点管理(`Daemon`)
- [ ] 文件管理(`File`)
- [ ] 镜像管理(`Image`)

## 支持的 MCSM 版本

| MCSM 版本 | 支持状态 |
| :---: | :---: |
| 10.x | ✅ |

### 快速示例

```python
from mcsmapi import MCSMAPI

# 初始化
mcsm = MCSMAPI("https://example.com")

# 使用账号密码登录(API权限取决于账号权限)
mcsm.login("username", "password")

# 使用apikey登录(API权限取决于apikey权限)
mcsm.login_with_apikey("apikey")

# 获取仪表盘数据
overview = mcsm.overview()

# 获取 MCSM 版本
mcsm_version = mcsm.overview().version

```

## 贡献

如果您发现任何问题或有改进建议，欢迎提交 [Issue](https://github.com/molanp/mcsmapi/issues) 或者创建 [Pull Request](https://github.com/molanp/mcsmapi/pulls)。

## 许可

`mcsmapi` 使用 [MIT 许可证](https://opensource.org/licenses/MIT)。

请参阅 [LICENSE](LICENSE) 文件以获取更多信息。

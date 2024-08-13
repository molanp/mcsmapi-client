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

## 使用方法

### 示例代码

以下是如何使用 `mcsmapi` 的一些示例：

```python
from mcsmapi import overview

# 如果有apikey，使用apikey验证
client = Overview(url=" https://example.com/",apikey="your_api_key")

# 如果没有apikey，使用账号密码验证
client = Overview(url=" https://example.com/")
# 登录
client.login(username="your_username",password="your_password")

# 获取数据
response = client.getData()
print(response.json())
```

### 支持的功能

- [x] 登录 (`(func) login`)
- [x] 仪表盘数据(`(cls) Overview`)
- [x] 用户管理(`(cls) Users`)
- [x] 实例管理(`(cls) Instance`)
- [x] 节点管理(`(cls) Daemon`)
- [x] 文件管理(`(cls) File`)
- [x] 镜像管理(`(cls) Image`)

## 支持的 MCSM 版本

当前版本的 `mcsmapi-client` 支持以下 `MCSM` 版本：

- 10.2.1
- 10.1.0

## 兼容的 Python 版本

- Python 3.7 及以上版本。

## 贡献

如果您发现任何问题或有改进建议，欢迎提交 [Issue](https://github.com/molanp/mcsmapi-client/issues) 或者创建 [Pull Request](https://github.com/molanp/mcsmapi-client/pulls)。

## 许可

`mcsmapi-client` 使用 [MIT 许可证](https://opensource.org/licenses/MIT)。

请参阅 [LICENSE](LICENSE) 文件以获取更多信息。

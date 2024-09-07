# Overview 类

`Overview` 类表示一个与特定 API 端点进行交互的客户端。

## 属性

- `client (ApiClient)`: 用于发送请求的 API 客户端。

## 初始化

`Overview` 类在创建实例时会自动调用 `__init__` 方法进行初始化。

- **参数**:
  - `url (str)`: API 的基础 URL。
  - `apikey (str, optional)`: 用于身份验证的 API 密钥，默认值为 `None`。

## 方法 `get_data`

```python
def get_data(self) -> requests.Response
```
**说明**: 从 API 获取概述数据。

- **返回**:
    - `requests.Response`: 由 API 返回的数据响应对象。
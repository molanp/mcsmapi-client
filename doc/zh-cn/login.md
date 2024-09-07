#### `login(username, password)`

- **功能**：
  - `login` 函数可被任何类调用，以实现向 MCSM 平台的登录操作。

- **效果**：
  - 成功登录后，将更新 `mcsmapi.ApiClient` 实例，并自动在后续的所有 API 请求中附带认证 token。

- **异常处理**：
  - 如果登录失败，则会抛出 `ValidateError` 异常。
  - 此异常继承自 `Exception` 类，并且会携带服务器返回的具体错误信息。

- **注意事项**：
  - 确保传入有效的用户名和密码以避免认证失败。
#### `login(username, password)`

- **Function**:
  - The `login` function can be called by any class to implement a login operation to the MCSM platform.

- **Effects**:
  - Upon successful login, the `mcsmapi.ApiClient` instance will be updated and the authentication token will be automatically attached to all subsequent API requests.

- **Exception Handling**:
  - If login fails, a `ValidateError` exception is thrown.
  - This exception inherits from the `Exception` class and carries a specific error message from the server.

- **Cautions**:
  - Make sure to pass in a valid username and password to avoid authentication failures.
# Daemon Class

The `Daemon` class represents a client that interacts with a particular daemon service.

## Attributes

- `client (ApiClient)`: The API client used to send requests.

## Initialization

The `Daemon` class is automatically initialized by calling the `__init__` method when an instance is created.

- **Parameters**.
  - `url (str)`: The base URL of the daemon service.
  - `apikey (str, optional)`: API key for authentication, defaults to `None`.

## Methods

### `getList`

```python
def getList(self) -> list
```
**Description**: Get a list of remote services.

- **Returns**.
    - ``list``: List of remote services.

### `add`:
```python
def add(self, ip: str, port: int, remarks: str, apiKey: str, prefix: str = “”) -> requests.Response
```
**Description**: Adds a new remote service.

- **Parameters**.

    - `ip (str)`: IP address of the remote service.
    - `port (int)`: The port number of the remote service.
    - `remarks (str)`: Remarks or description of the remote service.
    - `apiKey (str)`: API key of the remote service.
    - `prefix (str, optional)`: The optional prefix of the remote service, default is empty.
- **Returns**: `requests.

    - `requests.Response`: The response data returned by the server.

### `delete`:
```python
def delete(self, uuid: str) -> requests.Response
```
**Description**: Delete a remote service based on its UUID.

- **Parameters**.

    - `uuid (str)`: UUID of the remote service to delete.
- **Returns**: `requests.

    - `requests.Response`: The response data returned by the server.


### `tryConnect`
```python
def tryConnect(self, uuid: str, return_bool: bool = False) -> requests.Response || bool
```
**Description**: Try to connect to the remote service with the specified UUID.

- **Parameters**.

    - `uuid (str)`: The UUID of the remote service to connect to.
    - `return_bool (bool)`: Whether to return only the connection status boolean, defaults to `False`.
- **Return**:

    - `requests.Response || bool`: A boolean of the response data or node can status returned by the server.

### `updateDaemonConnectConfig`
```python
def updateDaemonConnectConfig(self, uuid: str, ip: str, port: int, remarks: str, apiKey: str, available: bool = False, prefix: str = “”) -> requests. Response
```
**Description**: Updates the configuration of the remote service.

- **Parameters**.

    - `uuid (str)`: UUID of the remote service to update.
    - `ip (str)`: The new IP address.
    - `port (int)`: The new port number.
    - `remarks (str)`: The new remarks or description.
    - `apiKey (str)`: The new API key.
    - `available (bool, optional)`: if the service is available, defaults to `False.
    - `prefix (str, optional):` The optional prefix, defaults to an empty string.
- **Returns**: `requests.

    - `requests.Response`: The response data returned by the server.
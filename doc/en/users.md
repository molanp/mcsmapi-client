# The Users Class

The `Users` class represents a client that interacts with a specific API endpoint to manage users.

## Properties

- `client (ApiClient)`: The API client used to send the request.

## Initialization

The `Users` class is automatically initialized by calling the `__init__` method when an instance is created.

- **Parameters**.
  - `url (str)`: The base URL of the API.
  - `apikey (str, optional)`: API key for authentication, defaults to `None`.

## Methods

### `get_list`

```python
def get_list(self, username: str = “”, page: int = 1, page_size: int = 10, role: str = “”) -> requests.Response
```
**Description**: Get a list of users from the API.

- **Parameters**.

    - `username (str, optional)`: The username to search for, defaults to empty string.
    - `page (int, optional)`: the page number to paginate, default is 1.
    - `page_size (int, optional)`: number of items per page, default is 10.
    - `role (str, optional)`: role to filter by, default is empty string.
- **Returns**.

    - `requests.Response`: The list of users returned by the API.

### `create`: 
```python
def create(self, username: str, password: str, permission: int = 1) -> requests.Response
```
**Description**: Creates a new user.

- **Parameters**.

    - `username (str)`: Username of the new user.
    - `password (str)`: Password for the new user.
    - `permission (int, optional)`: the permission level of the new user, default is 1.
- **Returns**: `requests.

    - `requests.Response`: The response returned by the API after creating the user.

### `update`
```python
def update(self, uuid: str, config: dict = {}) -> requests.Response
```
**Description**: Update an existing user.

- **Parameters**.

    - `uuid (str)`: UUID of the user to update.
    - `config (dict, optional)`: The user's configuration to update, defaults to an empty dictionary.
- **Returns**:

    - `requests.Response`: The response returned by the API after updating the user.

#### `delete`:
```python
def delete(self, uuids: list = []) -> requests.Response
```
**Description**: Delete one or more users.

- **Parameters**.

    - `uuids (list, optional)`: list of UUIDs of users to delete, defaults to an empty list.
- **Returns**: `requests.

    - `requests.Response`: The response returned by the API after deleting a user.
# `Users` Class

This class manages user-related operations in the API. It provides methods to search, create, update, and delete user accounts via the API.

## Initialization

```python
from mcsmapi import MCSMAPI

# Log in using an API key (API permissions depend on the provided API key)
mcsm = MCSMAPI("https://example.com").login_with_apikey("apikey")

users_manager = mcsm.users()
```

---

## Methods

### `search`

Search for user information based on the username and role.

**Parameters:**
- `username` (str): The username to search for. Defaults to an empty string, which means no filtering by username.
- `page` (int): The page number to specify which page of data to return. Defaults to `1`, which returns the first page.
- `page_size` (int): The number of results per page. Defaults to `20`, which means each page will contain 20 results.
- `role` (str): The role of the user. Defaults to an empty string, which means no filtering by role.

**Returns:**
- `dict`: A dictionary containing the search results. This includes a list of users that match the search criteria, as well as pagination info (total records, total pages, etc.).

**Code Example:**
```python
users_manager.search()
```

### `create`

Create a new user. This method takes the username, password, and permission level as parameters. If the user is successfully created, it will return the user’s unique identifier (UUID) or `True`, depending on the MCSM version.

**Parameters:**
- `username` (str): The username (string).
- `password` (str): The password (string).
- `permission` (int): The permission level (integer), default is `1`.

**Returns:**
- `str | bool`: The UUID of the newly created user or `True` upon success.

**Code Example:**
```python
users_manager.create("username", "password")
```

### `update`

Update user information.

> [!Important]
> If you need to update non-instance configuration data, first use the `search` method to fetch the full user details, modify the necessary fields, and pass the updated data as the `config` parameter to the `update` method.
> 
> When updating a user's instance resources, just pass in the corresponding instance list

**Parameters:**
- `uuid` (str): The unique identifier (UUID) of the user.
- `config` (dict | None): A dictionary containing the updated user information. Defaults to `None`.

**Returns:**
- `bool`: Returns `True` if the update was successful.

**Code Example:**
```python
users_manager.update("b7b5bc87eb454b52bbccc7f6c99dc333")
```

### `delete`

Delete a user.

**Parameters:**
- `uuids` (list | None): A list of UUIDs for users to be deleted. Defaults to `None`.

**Returns:**
- `bool`: Returns `True` if the deletion was successful.

**Code Example:**
```python
users_manager.delete(["b7b5bc87eb454b52bbccc7f6c99dc333"])
```

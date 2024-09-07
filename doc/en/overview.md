# Overview Class

The `Overview` class represents a client that interacts with a specific API endpoint.

## Attributes

- `client (ApiClient)`: The API client used to send the request.

## Initialization

The `Overview` class is automatically initialized by calling the `__init__` method when an instance is created.

- **Parameters**.
  - `url (str)`: The base URL of the API.
  - `apikey (str, optional)`: API key for authentication, defaults to `None`.

## method `get_data`

```python
def get_data(self) -> requests.Response
```
**Description**: Get overview data from the API.

- **Returns**.
    - `requests.Response`: The data response object returned by the API.

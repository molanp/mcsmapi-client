from .common import support_login, ApiClient
import requests


@support_login
class Overview:
    """
    Represents an overview client that interacts with an API endpoint.

    Attributes:
        client (ApiClient): The API client used for making requests.

    Args:
        url (str): The base URL of the API.
        apikey (str, optional): The API key for authentication. Defaults to None.
    """

    def __init__(self, url: str, apikey: str = None):
        """
        Initializes a new instance of the Overview class.

        Args:
            url (str): The base URL of the API.
            apikey (str, optional): The API key for authentication. Defaults to None.
        """
        self.client = ApiClient(url, apikey)

    def get_data(self) -> requests.Response:
        """
        Retrieves overview data from the API.

        Returns:
            dict: The overview data as returned by the API.
        """
        return self.client.send("GET", "overview")

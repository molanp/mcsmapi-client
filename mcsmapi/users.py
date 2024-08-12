from .common import support_login, ApiClient
import requests


@support_login
class Users:
    """
    Represents a users client that interacts with an API endpoint for user management.

    Attributes:
        client (ApiClient): The API client used for making requests.

    Args:
        url (str): The base URL of the API.
        apikey (str, optional): The API key for authentication. Defaults to None.
    """

    def __init__(self, url: str, apikey: str = None):
        """
        Initializes a new instance of the Users class.

        Args:
            url (str): The base URL of the API.
            apikey (str, optional): The API key for authentication. Defaults to None.
        """
        self.client = ApiClient(url, apikey)

    def get_list(self, username: str = "", page: int = 1, page_size: int = 10, role: str = "") -> requests.Response:
        """
        Retrieves a list of users from the API.

        Args:
            username (str, optional): The username to search for. Defaults to "".
            page (int, optional): The page number for pagination. Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 10.
            role (str, optional): The role to filter by. Defaults to "".

        Returns:
            dict: The list of users as returned by the API.
        """
        return self.client.send("GET", "auth/search", params={
            "userName": username, "page": page, "page_size": page_size, "role": role})

    def create(self, username: str, password: str, permission: int = 1) -> requests.Response:
        """
        Creates a new user.

        Args:
            username (str): The username for the new user.
            password (str): The password for the new user.
            permission (int, optional): The permission level for the new user. Defaults to 1.

        Returns:
            dict: The response from the API after creating the user.
        """
        return self.client.send("POST", "auth", data={
            "username": username, "password": password, "permission": permission})

    def update(self, uuid: str, config: dict = {}) -> requests.Response:
        """
        Updates an existing user.

        Args:
            uuid (str): The UUID of the user to update.
            config (dict, optional): The configuration updates for the user. Defaults to {}.

        Returns:
            dict: The response from the API after updating the user.
        """
        return self.client.send("PUT", "auth", data={
            "uuid": uuid, "config": config})

    def delete(self, uuids: list = []) -> requests.Response:
        """
        Deletes one or more users.

        Args:
            uuids (list, optional): A list of UUIDs of the users to delete. Defaults to [].

        Returns:
            dict: The response from the API after deleting the users.
        """
        return self.client.send("DELETE", "auth", data=uuids)

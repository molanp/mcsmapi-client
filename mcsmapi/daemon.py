from .common import support_login, ApiClient
import requests


@support_login
class Daemon:
    def __init__(self, url: str, apikey: str = None):
        """
        Initialize a new Daemon instance.

        :param url: The URL of the daemon service.
        :param apikey: Optional API key for authentication.
        """
        self.client = ApiClient(url, apikey)

    def getList(self) -> list:
        """
        Get a list of remote services.

        :return: A list of remote services.
        """
        return self.client.send("GET", "overview").json()["data"]["remote"]

    def add(self, ip: str, port: int, remarks: str, apiKey: str, prefix: str = "") -> requests.Response:
        """
        Add a new remote service.

        :param ip: IP address of the remote service.
        :param port: Port number of the remote service.
        :param remarks: Remarks or description of the remote service.
        :param apiKey: API key for the remote service.
        :param prefix: Optional prefix for the remote service.
        :return: Response data from the server.
        """
        return self.client.send(
            "POST", "service/remote_service", data={
                "ip": ip,
                "port": port,
                "prefix": prefix,
                "remarks": remarks,
                "apiKey": apiKey
            })

    def delete(self, uuid: str) -> requests.Response:
        """
        Delete a remote service by its UUID.

        :param uuid: UUID of the remote service to delete.
        :return: Response data from the server.
        """
        return self.client.send(
            "DELETE", "service/remote_service", params={"uuid": uuid})

    def tryConnect(self, uuid: str) -> requests.Response:
        """
        Try to connect to a remote service by its UUID.

        :param uuid: UUID of the remote service to connect to.
        :return: Response data from the server.
        """
        return self.client.send(
            "GET", "service/link_remote_service", params={"uuid": uuid})

    def updateDaemonConnectConfig(self, uuid: str, ip: str, port: int, remarks: str, apiKey: str, available: bool = False, prefix: str = "") -> requests.Response:
        """
        Update the configuration of a remote service.

        :param uuid: UUID of the remote service to update.
        :param ip: New IP address of the remote service.
        :param port: New port number of the remote service.
        :param remarks: New remarks or description of the remote service.
        :param apiKey: New API key for the remote service.
        :param available: Whether the service is available.
        :param prefix: Optional prefix for the remote service.
        :return: Response data from the server.
        """
        return self.client.send(
            "PUT", "service/remote_service", data={
                "uuid": uuid,
                "ip": ip,
                "port": port,
                "prefix": prefix,
                "available": available,
                "remarks": remarks,
                "apiKey": apiKey
            })

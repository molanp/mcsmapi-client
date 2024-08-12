from .common import support_login, ApiClient
import requests


@support_login
class Image:
    def __init__(self, url: str, apikey: str = None):
        """
        Initializes a new Image instance.

        Args:
            url (str): The URL of the image service.
            apikey (str, optional): Optional API key for authentication. Defaults to None.
        """
        self.client = ApiClient(url, apikey)

    def getImageList(self, daemonId: str) -> requests.Response:
        """
        Retrieves a list of Docker images.

        DockerImageList:
        https://docs.docker.com/engine/api/v1.37/#tag/Image/operation/ImageList

        Args:
            daemonId (str): ID of the Docker daemon.

        Returns:
            dict: Response data containing the list of Docker images.
        """

        return self.client.send("GET", "environment/image", params={
            "daemonId": daemonId
        })

    def getContainerList(self, daemonId: str) -> requests.Response:
        """
        Retrieves a list of Docker containers.

        DockerContainerList:
        https://docs.docker.com/engine/api/v1.37/#tag/Container/operation/ContainerList

        Args:
            daemonId (str): ID of the Docker daemon.

        Returns:
            dict: Response data containing the list of Docker containers.
        """

        return self.client.send("GET", "environment/containers", params={
            "daemonId": daemonId
        })

    def getNetworkModeList(self, daemonId: str) -> requests.Response:
        """
        Retrieves a list of Docker network modes.

        DockerNetworkModeList:
        https://docs.docker.com/engine/api/v1.37/#tag/Network/operation/NetworkList

        Args:
            daemonId (str): ID of the Docker daemon.

        Returns:
            dict: Response data containing the list of Docker network modes.
        """

        return self.client.send("GET", "environment/network", params={
            "daemonId": daemonId
        })

    def createImage(self, daemonId: str, dockerFileConfig: dict, imageName: str, tag: str) -> requests.Response:
        """
        Builds a Docker image from a Dockerfile configuration.

        Args:
            daemonId (str): ID of the Docker daemon.
            dockerFileConfig (dict): Configuration for the Dockerfile.
            imageName (str): Name of the Docker image.
            tag (str): Tag for the Docker image.

        Returns:
            dict: Response data indicating the status of the build process.
        """
        return self.client.send("POST", "environment/image", params={
            "daemonId": daemonId
        }, data={
            "dockerFile": dockerFileConfig,
            "imageName": imageName,
            "tag": tag
        })

    def buildProgress(self, daemonId: str) -> requests.Response:
        """
        Retrieves the progress of a Docker image build.

        Args:
            daemonId (str): ID of the Docker daemon.

        Returns:
            dict: Response data containing the build progress information.
        """
        return self.client.send("GET", "environment/image/progress", params={
            "daemonId": daemonId
        })

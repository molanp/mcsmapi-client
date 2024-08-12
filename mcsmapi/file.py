from .common import support_login, ApiClient
import aiohttp
import requests
import os


@support_login
class File:
    def __init__(self, url: str, apikey: str = None):
        """
        Initialize a new File instance.

        :param url: The URL of the file service.
        :param apikey: Optional API key for authentication.
        """
        self.client = ApiClient(url, apikey)

    def getList(self, daemonId: str, instanceUuid: str, target: str, page: int = 1, page_size: int = 10) -> requests.Response:
        """
        Get a list of files.

        :param daemonId: ID of the daemon.
        :param instanceUuid: UUID of the instance.
        :param target: Target directory path.
        :param page: Page number (default is 1).
        :param page_size: Number of items per page (default is 10).
        :return: Response data from the server.
        """
        return self.client.send("GET", "files/list", params={
            "daemonId": daemonId,
            "uuid": instanceUuid,
            "target": target,
            "page": page,
            "page_size": page_size
        })

    def getContents(self, daemonId: str, instanceUuid: str, target: str) -> requests.Response:
        """
        Get the contents of a file.

        :param daemonId: ID of the daemon.
        :param instanceUuid: UUID of the instance.
        :param target: Path to the file.
        :return: Response data from the server.
        """
        return self.client.send("PUT", "files", params={
            "daemonId": daemonId,
            "uuid": instanceUuid
        }, data={"target": target})

    def update(self, daemonId: str, instanceUuid: str, target: str, text: str) -> requests.Response:
        """
        Update the contents of a file.

        :param daemonId: ID of the daemon.
        :param instanceUuid: UUID of the instance.
        :param target: Path to the file.
        :param text: New content for the file.
        :return: Response data from the server.
        """
        return self.client.send("PUT", "files", params={
            "daemonId": daemonId,
            "uuid": instanceUuid
        }, data={"target": target, "text": text})

    def download(self, daemonId: str, instanceUuid: str, file_name: str, download_to_path: str) -> str:
        """
        Download a file from the server.

        :param daemonId: ID of the daemon.
        :param instanceUuid: UUID of the instance.
        :param file_name: Name of the file to download.
        :param download_to_path: Local path where the file will be saved.
        :return: Path to the downloaded file.
        """
        seq = self.client.send("POST", "files/download", params={
            "daemonId": daemonId,
            "uuid": instanceUuid,
            "file_name": file_name
        }).json()
        password = seq["password"]
        addr = seq["addr"]

        response = requests.get(
            f"http://{addr}/download/{password}/{file_name}", stream=True)
        if response.status_code == 200:
            file_path = os.path.join(download_to_path, file_name)
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            return file_path
        else:
            raise Exception(
                f"Failed to download file. Status code: {response.status_code}")

    async def aiodownload(self, daemonId: str, instanceUuid: str, file_name: str, download_to_path: str) -> str:
        """
        Asynchronously download a file from the server.

        :param daemonId: ID of the daemon.
        :param instanceUuid: UUID of the instance.
        :param file_name: Name of the file to download.
        :param download_to_path: Local path where the file will be saved.
        :return: Path to the downloaded file.
        """
        seq = self.client.send("POST", "files/download", params={
            "daemonId": daemonId,
            "uuid": instanceUuid,
            "file_name": file_name
        }).json()
        password = seq["password"]
        addr = seq["addr"]

        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://{addr}/download/{password}/{file_name}") as response:
                if response.status == 200:
                    file_path = os.path.join(download_to_path, file_name)
                    async with open(file_path, "wb") as f:
                        await f.write(await response.read())
                    return file_path
                else:
                    raise Exception(
                        f"Failed to download file. Status code: {response.status}")

    def upload(self, daemonId: str, instanceUuid: str, upload_dir: str, file_data: bytes) -> bool:
        """
        Upload a file to the server.

        :param daemonId: ID of the daemon.
        :param instanceUuid: UUID of the instance.
        :param upload_dir: Directory on the server where the file will be uploaded.
        :param file_data: Binary data of the file to upload.
        :return: True if the upload was successful.
        """
        seq = self.client.send("POST", "files/upload", params={
            "daemonId": daemonId,
            "uuid": instanceUuid,
            "upload_dir": upload_dir
        }).json()
        password = seq["password"]
        addr = seq["addr"]

        response = requests.post(
            f"http://{addr}/upload/{password}", files={"file": file_data})

        if response.status_code == 200:
            return True
        else:
            raise Exception(
                f"Failed to upload file. Status code: {response.status_code}")

    async def aioupload(self, daemonId: str, instanceUuid: str, upload_dir: str, file_data: bytes) -> bool:
        """
        Asynchronously upload a file to the server.

        :param daemonId: ID of the daemon.
        :param instanceUuid: UUID of the instance.
        :param upload_dir: Directory on the server where the file will be uploaded.
        :param file_data: Binary data of the file to upload.
        :return: True if the upload was successful.
        """
        seq = self.client.send("POST", "files/upload", params={
            "daemonId": daemonId,
            "uuid": instanceUuid,
            "upload_dir": upload_dir
        }).json()
        password = seq["password"]
        addr = seq["addr"]
        async with aiohttp.ClientSession() as session:
            async with session.post(f"http://{addr}/upload/{password}", data={"file": file_data}) as response:
                if response.status == 200:
                    return True
                else:
                    raise Exception(
                        f"Failed to upload file. Status code: {response.status}")

    def copy(self, daemonId: str, instanceUuid: str, source_list: list, target_list: list) -> requests.Response:
        """
        Copy files from one location to another.

        :param daemonId: ID of the daemon.
        :param instanceUuid: UUID of the instance.
        :param source_list: List of source file paths.
        :param target_list: List of target file paths.
        :return: Response data from the server.
        """
        data = {
            "targets": [
                [source, target] for source, target in zip(source_list, target_list)
            ]
        }

        return self.client.send("POST", "files/copy", params={
            "daemonId": daemonId,
            "uuid": instanceUuid
        }, data=data)

    def moveOrRename(self, daemonId: str, instanceUuid: str, source_list: list, target_list: list) -> requests.Response:
        """
        Move or rename files.

        :param daemonId: ID of the daemon.
        :param instanceUuid: UUID of the instance.
        :param source_list: List of source file paths.
        :param target_list: List of target file paths.
        :return: Response data from the server.
        """
        data = {
            "targets": [
                [source, target] for source, target in zip(source_list, target_list)
            ]
        }
        return self.client.send("PUT", "files/move", params={
            "daemonId": daemonId,
            "uuid": instanceUuid
        }, data=data)

    def zip(self, daemonId: str, instanceUuid: str, zip_file_path: str, targets: list) -> requests.Response:
        """
        Compress files into a ZIP archive.

        :param daemonId: ID of the daemon.
        :param instanceUuid: UUID of the instance.
        :param zip_file_path: Path to the resulting ZIP file.
        :param targets: List of files to compress.
        :return: Response data from the server.
        """
        zip_file_path = os.path.join(zip_file_path)

        return self.client.send("POST", "files/compress", params={
            "daemonId": daemonId,
            "uuid": instanceUuid
        }, data={
            "type": 1,
            "code": "utf-8",
            "source": zip_file_path,
            "targets": targets
        })

    def unzip(self, daemonId: str, instanceUuid: str, zip_file_path: str, unzip_to: str, code: str = "utf-8") -> requests.Response:
        """
        Decompresses a ZIP file.

        Args:
            daemonId (str): ID of the daemon.
            instanceUuid (str): UUID of the instance.
            zip_file_path (str): Path to the ZIP file.
            unzip_to (str): Directory path to extract the files to.
            code (str, optional): Encoding type. Defaults to "utf-8". Must be one of "utf-8", "gbk", or "big5".

        Returns:
            requests.Response: Response data from the server.

        Raises:
            ValueError: If the provided encoding type is not valid.
        """
        if code not in ["utf-8", "gbk", "big5"]:
            raise ValueError(
                "code must be one of utf-8, gbk, big5")
        return self.client.send("POST", "files/compress", params={
            "daemonId": daemonId,
            "uuid": instanceUuid
        }, data={
            "type": 2,
            "code": code,
            "source": zip_file_path,
            "target": unzip_to
        })

    def delete(self, daemonId: str, instanceUuid: str, targets: list) -> requests.Response:
        """
        Deletes files or directories.

        Args:
            daemonId (str): ID of the daemon.
            instanceUuid (str): UUID of the instance.
            targets (list): List of paths to the files or directories to delete.

        Returns:
            requests.Response: Response data from the server.
        """
        return self.client.send("DELETE", "files", params={
            "daemonId": daemonId,
            "uuid": instanceUuid
        }, data={
            "targets": targets
        })

    def touch(self, daemonId: str, instanceUuid: str, target: str) -> requests.Response:
        """
        Creates an empty file.

        Args:
            daemonId (str): ID of the daemon.
            instanceUuid (str): UUID of the instance.
            target (str): Path to the file to create.

        Returns:
            requests.Response: Response data from the server.
        """
        return self.client.send("POST", "files/touch", params={
            "daemonId": daemonId,
            "uuid": instanceUuid
        }, data={
            "target": target
        })

    def createFolder(self, daemonId: str, instanceUuid: str, target: str) -> requests.Response:
        """
        Creates a directory.

        Args:
            daemonId (str): ID of the daemon.
            instanceUuid (str): UUID of the instance.
            target (str): Path to the directory to create.

        Returns:
            requests.Response: Response data from the server.
        """
        return self.client.send("POST", "files/mkdir", params={
            "daemonId": daemonId,
            "uuid": instanceUuid
        }, data={
            "target": target
        })

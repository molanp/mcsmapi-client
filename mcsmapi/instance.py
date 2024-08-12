from .common import support_login, ApiClient
import requests


@support_login
class Instance:
    def __init__(self, url: str, apikey: str = None):
        """
        Initializes a new Instance object.

        Args:
            url (str): The URL of the service endpoint.
            apikey (str, optional): Optional API key for authentication. Defaults to None.
        """
        self.client = ApiClient(url, apikey)

    def getList(self, daemonId: str, page: int = 1, page_size: int = 10, instance_name: str = "", status: str = "") -> requests.Response:
        """
        Retrieves a list of instances.

        Args:
            daemonId (str): ID of the daemon.
            page (int, optional): Page number for pagination. Defaults to 1.
            page_size (int, optional): Number of items per page. Defaults to 10.
            instance_name (str, optional): Filter by instance name. Defaults to "".
            status (str, optional): Filter by instance status. Defaults to "".

        Returns:
            requests.Response: Response data containing the list of instances.
        """
        return self.client.send("GET", "service/remote_service_instances", params={
            "daemonId": daemonId, "page": page, "page_size": page_size,
            "instance_name": instance_name, "status": status})

    def detail(self, instanceUuid: str, daemonId: str) -> requests.Response:
        """
        Retrieves details of a specific instance.

        Args:
            instanceUuid (str): UUID of the instance.
            daemonId (str): ID of the daemon.

        Returns:
            requests.Response: Response data containing the details of the instance.
        """
        return self.client.send("GET", "instance ", params={
            "uuid": instanceUuid, "daemonId": daemonId})

    def create(self, daemonId: str, InstanceConfig: requests.Response) -> requests.Response:
        """
        Creates a new instance.

        Args:
            daemonId (str): ID of the daemon.
            InstanceConfig (requests.Response): Configuration for the new instance.

        Returns:
            requests.Response: Response data indicating the creation status.
        """
        return self.client.send("POST", "instance", params={
            "daemonId": daemonId}, data=InstanceConfig)

    def updateConfig(self, instanceUuid: str, daemonId: str, InstanceConfig: requests.Response) -> requests.Response:
        """
        Updates the configuration of an existing instance.

        Args:
            instanceUuid (str): UUID of the instance.
            daemonId (str): ID of the daemon.
            InstanceConfig (requests.Response): Updated configuration for the instance.

        Returns:
            requests.Response: Response data indicating the update status.
        """
        return self.client.send("POST", "instance", params={
            "uuid": instanceUuid, "daemonId": daemonId}, data=InstanceConfig)

    def delete(self, daemonId: str, instanceUuids: list, delete_file: bool = False) -> requests.Response:
        """
        Deletes one or more instances.

        Args:
            daemonId (str): ID of the daemon.
            instanceUuids (list): List of UUIDs of the instances to delete.
            delete_file (bool, optional): Whether to delete associated files. Defaults to False.

        Returns:
            requests.Response: Response data indicating the deletion status.
        """
        return self.client.send("DELETE", "instance", params={
            "daemonId": daemonId}, data={"uuids": instanceUuids, "deleteFile": delete_file})

    def start(self, instanceUuid: str, daemonId: str) -> requests.Response:
        """
        Starts an instance.

        Args:
            instanceUuid (str): UUID of the instance.
            daemonId (str): ID of the daemon.

        Returns:
            requests.Response: Response data indicating the start status.
        """
        return self.client.send("GET", "protected_instance/open", params={
            "uuid": instanceUuid, "daemonId": daemonId})

    def stop(self, instanceUuid: str, daemonId: str) -> requests.Response:
        """
        Stops an instance.

        Args:
            instanceUuid (str): UUID of the instance.
            daemonId (str): ID of the daemon.

        Returns:
            requests.Response: Response data indicating the stop status.
        """
        return self.client.send("GET", "protected_instance/stop", params={
            "uuid": instanceUuid, "daemonId": daemonId})

    def restart(self, instanceUuid: str, daemonId: str) -> requests.Response:
        """
        Restarts an instance.

        Args:
            instanceUuid (str): UUID of the instance.
            daemonId (str): ID of the daemon.

        Returns:
            requests.Response: Response data indicating the restart status.
        """
        return self.client.send("GET", "protected_instance/restart", params={
            "uuid": instanceUuid, "daemonId": daemonId})

    def kill(self, instanceUuid: str, daemonId: str) -> requests.Response:
        """
        Kills an instance.

        Args:
            instanceUuid (str): UUID of the instance.
            daemonId (str): ID of the daemon.

        Returns:
            requests.Response: Response data indicating the kill status.
        """
        return self.client.send("GET", "protected_instance/kill", params={
            "uuid": instanceUuid, "daemonId": daemonId})

    def batchOperation(self, daemonId: str, instanceUuid: str, operations: str) -> requests.Response:
        """
        Performs a batch operation on instances.

        Args:
            daemonId (str): ID of the daemon.
            instanceUuid (str): UUID of the instance.
            operations (str): Operation to perform. Must be one of "start", "stop", "restart", "kill".

        Returns:
            requests.Response: Response data indicating the operation status.

        Raises:
            ValueError: If the operation is not one of the allowed values.
        """
        if operations not in ["start", "stop", "restart", "kill"]:
            raise ValueError(
                "operations must be one of start, stop, restart, kill")
        return self.client.send("POST", f"instance/multi_{operations}", params={
            "daemonId": daemonId, "instanceUuid": instanceUuid})

    def updateInstance(self, instanceUuid: str, daemonId: str, task_name: str) -> requests.Response:
        """
        Updates an instance with a specified task.

        Args:
            instanceUuid (str): UUID of the instance.
            daemonId (str): ID of the daemon.
            task_name (str): Name of the task to execute.

        Returns:
            requests.Response: Response data indicating the update status.
        """
        return self.client.send("GET", "protected_instance/asynchronous", params={
            "uuid": instanceUuid, "daemonId": daemonId, "task_name": task_name})

    def sendCommand(self, instanceUuid: str, daemonId: str, command: str) -> requests.Response:
        """
        Sends a command to an instance.

        Args:
            instanceUuid (str): UUID of the instance.
            daemonId (str): ID of the daemon.
            command (str): Command to send.

        Returns:
            requests.Response: Response data indicating the command status.
        """
        return self.client.send("POST", "protected_instance/command", params={
            "uuid": instanceUuid, "daemonId": daemonId, "command": command})

    def getOutput(self, instanceUuid: str, daemonId: str, size: int = None) -> requests.Response:
        """
        Retrieves output log from an instance.

        Args:
            instanceUuid (str): UUID of the instance.
            daemonId (str): ID of the daemon.
            size (int, optional): Number of log lines to retrieve. Defaults to None.

        Returns:
            requests.Response: Response data containing the output log.
        """
        params = {"uuid": instanceUuid, "daemonId": daemonId}
        if size is not None:
            params["size"] = size
        return self.client.send(
            "GET", "protected_instance/outputlog", params=params)

    def reinstall(self, uuid: str, daemonId: str, targetUrl: str, title: str, description: str = "") -> requests.Response:
        """
        Reinstalls an instance.

        Args:
            uuid (str): UUID of the instance.
            daemonId (str): ID of the daemon.
            targetUrl (str): Target URL for the installation.
            title (str): Title of the instance.
            description (str, optional): Description of the instance. Defaults to "".

        Returns:
            requests.Response: Response data indicating the reinstall status.
        """
        return self.client.send("GET", "protected_instance/install_instance", params={
            "uuid": uuid, "daemonId": daemonId}, data={"targetUrl": targetUrl, "title": title, "description": description})

    def typeOfInstanceConfig(self, **kwargs) -> dict:
        """
        Generates an instance configuration based on the provided arguments.

        Args:
            **kwargs: Keyword arguments representing the configuration parameters.

        Returns:
            dict: An instance configuration dictionary.

        Raises:
            ValueError: If any unsupported keys are provided.

        Supported Keys:
            - nickname (str): Nickname of the instance.
            - startCommand (str): Start command for the instance.
            - stopCommand (str): Stop command for the instance.
            - cwd (str): Current working directory for the instance.
            - ie (str): Input encoding.
            - oe (str): Output encoding.
            - createDatetime (str): Creation datetime.
            - lastDatetime (str): Last updated datetime.
            - type (str): Type of the instance.
            - tag (list): Tags associated with the instance.
            - endTime (str): End time of the instance.
            - fileCode (str): File code.
            - processType (str): Process type.
            - updateCommand (str): Update command.
            - actionCommandList (list): List of action commands.
            - crlf (int): CRLF value.
            - docker (dict): Docker configuration.
            - enableRcon (bool): Enable RCON.
            - rconPassword (str): RCON password.
            - rconPort (int): RCON port.
            - rconIp (str): RCON IP address.
            - terminalOption (dict): Terminal options.
            - eventTask (dict): Event task settings.
            - pingConfig (dict): Ping configuration.
        """
        default = {
            "nickname": "New Name",
            "startCommand": "cmd.exe",
            "stopCommand": "^C",
            "cwd": "/workspaces/my_server/",
            "ie": "utf8",
            "oe": "gbk",
            "createDatetime": "2022/2/3",
            "lastDatetime": "2022/2/3 16:02",
            "type": "universal",
            "tag": [],
            "endTime": "2022/2/28",
            "fileCode": "gbk",
            "processType": "docker",
            "updateCommand": "shutdown -s",
            "actionCommandList": [],
            "crlf": 2,
            "docker": self.typeOfDockerConfig(),

            "enableRcon": True,
            "rconPassword": "123456",
            "rconPort": 2557,
            "rconIp": "192.168.1.233",

            "terminalOption": {
                "haveColor": False,
                "pty": True,
            },
            "eventTask": {
                "autoStart": False,
                "autoRestart": True,
                "ignore": False,
            },
            "pingConfig": {
                "ip": "",
                "port": 25565,
                "type": 1,
            }
        }

        supported_keys = set(default.keys())
        unsupported_keys = set(kwargs.keys()) - supported_keys

        if unsupported_keys:
            raise ValueError(
                f"Unsupported keys: {unsupported_keys}. Supported keys are: {supported_keys}")

        config = default.copy()
        config.update(kwargs)

        return config

    def typeOfDockerConfig(self, **kwargs) -> dict:
        """
        Generates a Docker configuration based on the provided arguments.

        Args:
            **kwargs: Keyword arguments representing the configuration parameters.

        Returns:
            dict: A Docker configuration dictionary.

        Raises:
            ValueError: If any unsupported keys are provided.

        Supported Keys:
            - containerName (str): Container name.
            - image (str): Docker image name.
            - memory (int): Memory limit in MB.
            - ports (list): Ports mapping.
            - extraVolumes (list): Extra volumes.
            - maxSpace (int): Maximum space.
            - network (str): Network mode.
            - io (int): IO limit.
            - networkMode (str): Network mode.
            - networkAliases (list): Network aliases.
            - cpusetCpus (str): CPU set.
            - cpuUsage (int): CPU usage.
            - workingDir (str): Working directory.
            - env (list): Environment variables.
        """
        default = {
            "containerName": "",
            "image": "mcsm-ubuntu:22.04",
            "memory": 1024,
            "ports": ["25565:25565/tcp"],
            "extraVolumes": [],
            "maxSpace": None,
            "network": None,
            "io": None,
            "networkMode": "bridge",
            "networkAliases": [],
            "cpusetCpus": "",
            "cpuUsage": 100,
            "workingDir": "",
            "env": []
        }

        supported_keys = set(default.keys())
        unsupported_keys = set(kwargs.keys()) - supported_keys

        if unsupported_keys:
            raise ValueError(
                f"Unsupported keys: {unsupported_keys}. Supported keys are: {supported_keys}")

        config = default.copy()
        config.update(kwargs)

        return config

# Unused functions
# ...

# Unused functions
#    def typeOfInstanceDetail(self, **kwargs):
#        default = {
#            "config": self.typeOfInstanceConfig(),
#            "info": {
#                "currentPlayers": -1,
#                "fileLock": 0,
#                "maxPlayers": -1,
#                "openFrpStatus": False,
#                "playersChart": [],
#                "version": "",
#            },
#            "instanceUuid": "50c73059001b436fa85c0d8221c157cf",
#            "processInfo": {
#                "cpu": 0,
#                "memory": 0,
#                "ppid": 0,
#                "pid": 0,
#                "ctime": 0,
#                "elapsed": 0,
#                "timestamp": 0
#            },
#            "space": 0,
#            "started": 6,
#            "status": 3,
#        }
#
#       supported_keys = set(default.keys())
#        unsupported_keys = set(kwargs.keys()) - supported_keys
#
#       if unsupported_keys:
#            raise ValueError(
#                f"Unsupported keys: {unsupported_keys}. Supported keys are: {supported_keys}")
#
#        config = default.copy()
#        config.update(kwargs)
#
#       return config

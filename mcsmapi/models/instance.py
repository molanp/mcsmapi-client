from typing import List, Dict, Optional
from pydantic import BaseModel
from mcsmapi.models.file import FileList
from mcsmapi.models.image import DockerConfig


class TerminalOption(BaseModel):
    haveColor: bool = False
    pty: bool = True


class EventTask(BaseModel):
    autoStart: bool = False
    autoRestart: bool = True
    ignore: bool = False


class PingConfig(BaseModel):
    ip: str = ""
    port: int = 25565
    type: int = 1


class InstanceConfig(BaseModel):
    nickname: str = "New Name"
    startCommand: str = "cmd.exe"
    stopCommand: str = "^C"
    cwd: str = ""
    ie: str = "gbk"  # 输入编码
    oe: str = "gbk"  # 输出编码
    createDatetime: int = 0
    lastDatetime: int = 0
    type: str = "universal"
    tag: List[str] = []
    endTime: Optional[int] = None
    fileCode: str = "gbk"
    processType: str = "docker"
    updateCommand: str = "shutdown -s"
    actionCommandList: List[str] = []
    crlf: int = 2
    docker: "DockerConfig" = DockerConfig()
    enableRcon: bool = True
    rconPassword: str = ""
    rconPort: int = 2557
    rconIp: str = ""
    terminalOption: TerminalOption = TerminalOption()
    eventTask: EventTask = EventTask()
    pingConfig: PingConfig = PingConfig()


class ProcessInfo(BaseModel):
    cpu: int = 0
    memory: int = 0
    ppid: int = 0
    pid: int = 0
    ctime: int = 0
    elapsed: int = 0
    timestamp: int = 0


class InstanceInfo(BaseModel):
    currentPlayers: int = -1
    fileLock: int = 0
    maxPlayers: int = -1
    openFrpStatus: bool = False
    playersChart: List[Dict] = []
    version: str = ""


class InstanceDetail(BaseModel):
    config: InstanceConfig = InstanceConfig()
    info: InstanceInfo = InstanceInfo()
    daemonId: str = ""
    instanceUuid: str = ""
    processInfo: ProcessInfo = ProcessInfo()
    space: int = 0
    started: int = 0  # 启动次数
    status: int = 0  # -1 = 忙碌, 0 = 停止, 1 = 停止中, 2 = 启动中, 3 = 运行中

    def start(self) -> str | bool:
        """
        启动该实例。

        **返回:**
        - str|bool: str|bool: 返回结果中的 "instanceUuid" 字段值，如果未找到该字段，则默认返回True。
        """
        from mcsmapi.apis.instance import Instance

        return Instance().start(self.daemonId, self.instanceUuid)

    def stop(self) -> str | bool:
        """
        停止该实例。

        **返回:**
        - str|bool: 返回结果中的 "instanceUuid" 字段值，如果未找到该字段，则默认返回True。
        """
        from mcsmapi.apis.instance import Instance

        return Instance().stop(self.daemonId, self.instanceUuid)

    def restart(self) -> str | bool:
        """
        重启该实例。

        **返回:**
        - str|bool: 返回结果中的 "instanceUuid" 字段值，如果未找到该字段，则默认返回True。
        """
        from mcsmapi.apis.instance import Instance

        return Instance().restart(self.daemonId, self.instanceUuid)

    def kill(self) -> str | bool:
        """
        强制关闭该实例。

        **返回:**
        - str|bool: 返回结果中的 "instanceUuid" 字段值，如果未找到该字段，则默认返回True。
        """
        from mcsmapi.apis.instance import Instance

        return Instance().kill(self.daemonId, self.instanceUuid)

    def delete(self, deleteFile=False) -> str:
        """
        删除该实例。

        **返回:**
        - str: 被删除的实例的uuid。
        """
        from mcsmapi.apis.instance import Instance

        return Instance().delete(self.daemonId, [self.instanceUuid], deleteFile)[0]

    def update(self) -> bool:
        """
        升级实例。

        **返回:**
        - bool: 返回操作结果，成功时返回True。
        """
        from mcsmapi.apis.instance import Instance

        return Instance().update(self.daemonId, self.instanceUuid)

    def updateConfig(self, config: dict) -> str | bool:
        """
        更新该实例配置。

        **参数:**
        - config (dict): 新的实例配置，以字典形式提供，缺失内容由使用原实例配置填充。

        **返回:**
        - str|bool: 更新成功后返回更新的实例UUID，如果未找到该字段，则默认返回True。
        """
        from mcsmapi.apis.instance import Instance

        updated_config = self.config.dict()
        updated_config.update(config)

        instance_config = InstanceConfig(**updated_config).dict()

        return Instance().updateConfig(
            self.daemonId, self.instanceUuid, instance_config
        )

    def reinstall(self, targetUrl: str, title: str = "", description: str = "") -> bool:
        """
        重装实例。

        **参数:**
        - targetUrl (str): 重装文件的目标URL。
        - title (str): 重装文件的标题。
        - description (str, optional): 重装文件的描述，默认为空字符串。

        **返回:**
        - bool: 返回操作结果，成功时返回True
        """
        from mcsmapi.apis.instance import Instance

        return Instance().reinstall(
            self.daemonId, self.instanceUuid, targetUrl, title, description
        )

    def files(self, target:str = "", page:int=0, page_size:int=100) -> FileList:
        """
        获取实例的文件列表。

        **参数:**
        - target (str, 可选): 用于文件过滤的目标路径。默认为空字符串，表示不按路径过滤
        - page (int, 可选): 指定分页的页码。默认为0。
        - page_size (int, 可选): 指定每页的文件数量。默认为100。

        **返回:**
        - FileList: 文件列表。
        """
        from mcsmapi.apis.file import File

        return File().show(self.daemonId, self.instanceUuid, target, page, page_size)


class InstanceCreateResult(BaseModel):
    instanceUuid: str = ""
    config: InstanceConfig = InstanceConfig()


class InstanceSearchList(BaseModel):
    pageSize: int = 0
    maxPage: int = 0
    data: List[InstanceDetail] = []
    daemonId: str = ""

    def __init__(self, **data: str):
        super().__init__(**data)
        for instance in self.data:
            instance.daemonId = self.daemonId


class UserInstancesList(BaseModel):
    instanceUuid: str = ""
    daemonId: str = ""

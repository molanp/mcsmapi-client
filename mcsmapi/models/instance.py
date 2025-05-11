from typing import List, Dict, Optional
from pydantic import BaseModel
from mcsmapi.models.file import FileList
from mcsmapi.models.image import DockerConfig


class TerminalOption(BaseModel):
    """终端选项"""

    """是否启用颜色输出"""
    haveColor: bool = False
    """是否使用伪终端 (PTY)"""
    pty: bool = True


class EventTask(BaseModel):
    """事件任务"""

    """是否自动启动"""
    autoStart: bool = False
    """是否自动重启"""
    autoRestart: bool = True
    """是否忽略该任务"""
    ignore: bool = False


class PingConfig(BaseModel):
    """服务器 Ping 配置"""

    """服务器 IP 地址"""
    ip: str = ""
    """服务器端口"""
    port: int = 25565
    """Ping 类型 (1: 默认类型)"""
    type: int = 1


class InstanceConfig(BaseModel):
    """实例配置信息"""

    """实例名称"""
    nickname: str = "New Name"
    """启动命令"""
    startCommand: str = "cmd.exe"
    """停止命令"""
    stopCommand: str = "^C"
    """工作目录"""
    cwd: str = ""
    """输入编码"""
    ie: str = "gbk"
    """输出编码"""
    oe: str = "gbk"
    """创建时间 (Unix 时间戳)"""
    createDatetime: int = 0
    """最后修改时间 (Unix 时间戳)"""
    lastDatetime: int = 0
    """实例类型 (universal, minecraft 等)"""
    type: str = "universal"
    """实例标签"""
    tag: List[str] = []
    """实例结束时间 (可选)"""
    endTime: Optional[int] = None
    """文件编码"""
    fileCode: str = "gbk"
    """进程类型 (如 docker, local)"""
    processType: str = "docker"
    """更新命令"""
    updateCommand: str = "shutdown -s"
    """实例可执行的操作命令列表"""
    actionCommandList: List[str] = []
    """换行符 (0: LF, 1: CR, 2: CRLF)"""
    crlf: int = 2
    """Docker 相关配置"""
    docker: "DockerConfig" = DockerConfig()
    """是否启用 RCON 远程控制"""
    enableRcon: bool = True
    """RCON 连接密码"""
    rconPassword: str = ""
    """RCON 端口"""
    rconPort: int = 2557
    """RCON IP 地址"""
    rconIp: str = ""
    """终端选项配置"""
    terminalOption: TerminalOption = TerminalOption()
    """事件任务配置"""
    eventTask: EventTask = EventTask()
    """服务器 Ping 监测配置"""
    pingConfig: PingConfig = PingConfig()


class ProcessInfo(BaseModel):
    """进程信息"""

    """CPU 使用率 (单位: %)"""
    cpu: int = 0
    """进程占用内存 (单位: KB)"""
    memory: int = 0
    """父进程 ID"""
    ppid: int = 0
    """进程 ID"""
    pid: int = 0
    """进程创建时间 (Unix 时间戳)"""
    ctime: int = 0
    """进程运行时长 (单位: 秒)"""
    elapsed: int = 0
    """时间戳"""
    timestamp: int = 0


class InstanceInfo(BaseModel):
    """实例运行状态信息( 这些选项在新版中已不再支持设置，但仍在API中返回)"""

    """当前玩家数量 (-1 表示未知)"""
    currentPlayers: int = -1
    """文件锁状态 (0: 无锁)"""
    fileLock: int = 0
    """最大允许玩家数 (-1 表示未知)"""
    maxPlayers: int = -1
    """是否启用 FRP 远程服务"""
    openFrpStatus: bool = False
    """玩家数量变化图表数据"""
    playersChart: List[Dict] = []
    """服务器版本"""
    version: str = ""


class InstanceDetail(BaseModel):
    """实例详细信息"""

    """实例的配置信息"""
    config: InstanceConfig = InstanceConfig()
    """实例的运行状态信息"""
    info: InstanceInfo = InstanceInfo()
    """所属的守护进程 (Daemon) ID"""
    daemonId: str = ""
    """实例唯一标识符 (UUID)"""
    instanceUuid: str = ""
    """实例的进程信息"""
    processInfo: ProcessInfo = ProcessInfo()
    """实例的存储空间大小(始终为`0`)"""
    space: int = 0  # 在 MCSM 代码中，此项始终为 0，意义不明
    """实例的启动次数"""
    started: int = 0
    """实例状态 (-1: 忙碌, 0: 停止, 1: 停止中, 2: 启动中, 3: 运行中)"""
    status: int = 0

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

    def files(self, target: str = "", page: int = 0, page_size: int = 100) -> FileList:
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
    """实例创建结果"""

    """实例唯一标识符 (UUID)"""
    instanceUuid: str = ""
    """实例的配置信息"""
    config: InstanceConfig = InstanceConfig()


class InstanceSearchList(BaseModel):
    """实例搜索列表"""

    """每页的实例数量"""
    pageSize: int = 0
    """最大页数"""
    maxPage: int = 0
    """实例详细信息列表"""
    data: List[InstanceDetail] = []
    """所属的守护进程 (Daemon) ID"""
    daemonId: str = ""

    def __init__(self, **data: str):
        """实例化对象，并在每个实例中填充 daemonId"""
        super().__init__(**data)
        for instance in self.data:
            instance.daemonId = self.daemonId


class UserInstancesList(BaseModel):
    """用户实例列表"""

    """实例唯一标识符 (UUID)"""
    instanceUuid: str = ""
    """所属的守护进程 (Daemon) ID"""
    daemonId: str = ""

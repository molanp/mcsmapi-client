from enum import IntEnum
from typing import Any, TypedDict
from pydantic import BaseModel
from mcsmapi.models.image import DockerConfig


class CRLFType(IntEnum):
    """换行符"""

    LF = 0
    CR = 1
    CRLF = 2


class Status(IntEnum):
    """实例状态"""

    BUSY = -1
    STOP = 0
    STOPPING = 1
    STARTING = 2
    RUNNING = 3


class batchOperationDetail(TypedDict):
    """批量操作的实例信息"""

    uuid: str
    """实例UUID"""
    daemonId: str
    """节点UUID"""


class TerminalOption(BaseModel):
    """终端选项"""

    haveColor: bool = False
    """是否启用前端颜色渲染"""
    pty: bool = True
    """是否使用伪终端 (PTY)"""
    ptyWindowCol: int = 164
    """PTY 窗口列数"""
    ptyWindowRow: int = 40
    """PTY 窗口行数"""


class EventTask(BaseModel):
    """事件任务"""

    autoStart: bool = False
    """是否自动启动"""
    autoRestart: bool = True
    """是否自动重启"""
    ignore: bool = False
    """是否忽略该任务"""


class PingConfig(BaseModel):
    """服务器 Ping 配置(已弃用)"""

    ip: str = ""
    """服务器 IP 地址"""
    port: int = 25565
    """服务器端口"""
    type: int = 1
    """Ping 类型 (0: UDP, 1: TCP)"""


class InstanceConfig(BaseModel):
    """实例配置信息"""

    nickname: str = "New Name"
    """实例名称"""
    startCommand: str = "cmd.exe"
    """启动命令"""
    stopCommand: str = "^C"
    """停止命令"""
    cwd: str = ""
    """工作目录"""
    ie: str = "utf8"
    """输入编码"""
    oe: str = "UTF-8"
    """输出编码"""
    createDatetime: int = 0
    """创建时间 (Unix 时间戳)"""
    lastDatetime: int = 0
    """最后修改时间 (Unix 时间戳)"""
    type: str = "universal"
    """实例类型 (universal, minecraft 等)"""
    tag: list[str] = []
    """实例标签"""
    endTime: int | None = None
    """实例到期时间"""
    fileCode: str = "utf8"
    """文件编码"""
    processType: str = "general"
    """进程类型 (如 docker, general)"""
    updateCommand: str = "shutdown -s"
    """更新命令"""
    actionCommandList: list[str] = []
    """实例可执行的操作命令列表"""
    crlf: CRLFType = CRLFType.CRLF
    """换行符"""
    docker: DockerConfig = DockerConfig()
    """Docker 相关配置"""
    enableRcon: bool = False
    """是否启用 RCON 远程控制"""
    rconPassword: str = ""
    """RCON 连接密码"""
    rconPort: int = 2557
    """RCON 端口"""
    rconIp: str = ""
    """RCON IP 地址"""
    terminalOption: TerminalOption = TerminalOption()
    """终端选项配置"""
    eventTask: EventTask = EventTask()
    """事件任务配置"""
    pingConfig: PingConfig = PingConfig()
    """服务器 Ping 监测配置(已弃用)"""
    runAs: str = ""
    """运行该实例的系统用户，为空则使用启动面板的系统用户"""


class InstanceProcessInfo(BaseModel):
    """进程信息"""

    cpu: int
    """CPU 使用率 (单位: %)"""
    memory: int
    """进程占用内存 (单位: KB)"""
    ppid: int
    """父进程 ID"""
    pid: int
    """进程 ID"""
    ctime: int
    """进程创建时间 (Unix 时间戳)"""
    elapsed: int
    """进程运行时长 (单位: 秒)"""
    timestamp: int
    """时间戳"""


class InstanceInfo(BaseModel):
    """实例运行状态信息(这些选项在新版中已不再支持设置，但仍在API中返回)"""

    currentPlayers: int
    """当前玩家数量"""
    fileLock: int = 0
    """文件锁状态 (0: 无锁)"""
    maxPlayers: int = -1
    """最大允许玩家数 (-1 表示未知)"""
    openFrpStatus: bool = False
    """是否启用 FRP 远程服务"""
    playersChart: list[dict] = []
    """玩家数量变化图表数据"""
    version: str = ""
    """服务器版本"""


class InstanceDetail(BaseModel):
    """实例详细信息"""

    config: InstanceConfig
    """实例的配置信息"""
    info: InstanceInfo
    """实例的运行状态信息"""
    daemonId: str
    """所属的节点UUID"""
    instanceUuid: str
    """实例UUID"""
    processInfo: InstanceProcessInfo
    """实例的进程信息"""
    started: int
    """实例的启动次数"""
    status: Status
    """实例状态"""

    def start(self):
        """
        启动该实例

        :returns: 返回被操作的实例的UUID
        """
        from mcsmapi.apis.instance import Instance

        return Instance.start(self.daemonId, self.instanceUuid)

    def stop(self):
        """
        停止该实例

        :returns: 返回被操作的实例的UUID
        """
        from mcsmapi.apis.instance import Instance

        return Instance.stop(self.daemonId, self.instanceUuid)

    def restart(self):
        """
        重启该实例

        :returns: 返回被操作的实例的UUID
        """
        from mcsmapi.apis.instance import Instance

        return Instance.restart(self.daemonId, self.instanceUuid)

    def kill(self):
        """
        强制关闭该实例

        :returns: 返回被操作的实例的UUID
        """
        from mcsmapi.apis.instance import Instance

        return Instance.kill(self.daemonId, self.instanceUuid)

    def delete(self, deleteFile=False):
        """
        删除该实例

        :returns: 被删除的实例的uuid
        """
        from mcsmapi.apis.instance import Instance

        return Instance.delete(self.daemonId, [self.instanceUuid], deleteFile)[0]

    def update(self):
        """
        升级实例

        :returns: 操作成功返回True
        """
        from mcsmapi.apis.instance import Instance

        return Instance.update(self.daemonId, self.instanceUuid)

    def updateConfig(self, config: dict[str, Any]):
        """
        更新该实例配置

        :params config: 新的实例配置，以字典形式提供，缺失内容由使用原实例配置填充

        :returns: 更新成功后返回更新的实例UUID
        """
        from mcsmapi.apis.instance import Instance

        updated_config = self.config.model_dump()
        updated_config.update(config)

        instance_config = InstanceConfig(**updated_config).model_dump()

        return Instance.updateConfig(self.daemonId, self.instanceUuid, instance_config)

    def reinstall(self, targetUrl: str, title: str = "", description: str = ""):
        """
        重装实例

        :params targetUrl: 重装文件的目标URL
        :params title: 重装文件的标题
        :params description: 重装文件的描述，默认为空字符串

        :returns: 操作成功返回True
        """
        from mcsmapi.apis.instance import Instance

        return Instance.reinstall(
            self.daemonId, self.instanceUuid, targetUrl, title, description
        )

    def files(
        self, target: str = "", page: int = 0, page_size: int = 100, file_name: str = ""
    ):
        """
        获取实例的文件列表

        :params target: 用于文件过滤的目标路径默认为空字符串，表示不按路径过滤
        :params page: 指定分页的页码
        :params page_size: 指定每页的文件数量
        :params file_name: 用于在文件列表中过滤出名称包含指定字符串的文件或文件夹

        :returns: 文件列表
        """
        from mcsmapi.apis.file import File

        return File.show(
            self.daemonId, self.instanceUuid, target, page, page_size, file_name
        )


class InstanceCreateResult(BaseModel):
    """实例创建结果"""

    instanceUuid: str = ""
    """实例UUID"""
    config: InstanceConfig = InstanceConfig()
    """实例的配置信息"""


class InstanceSearchList(BaseModel):
    """实例搜索列表"""

    pageSize: int = 0
    """每页的实例数量"""
    maxPage: int = 0
    """最大页数"""
    data: list[InstanceDetail] = []
    """实例详细信息列表"""
    daemonId: str = ""
    """所属的节点UUID"""

    def __init__(self, **data: str):
        """实例化对象，并在每个实例中填充 daemonId"""
        super().__init__(**data)
        for instance in self.data:
            instance.daemonId = self.daemonId


class UserInstancesList(BaseModel):
    """用户实例列表"""

    instanceUuid: str = ""
    """实例UUID"""
    daemonId: str = ""
    """所属的节点UUID"""

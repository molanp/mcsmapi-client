from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class DockerConfig:
    containerName: str = ""
    image: str = ""
    memory: int = 1024  # in MB
    ports: List[str] = field(default_factory=list)
    extraVolumes: List[str] = field(default_factory=list)
    maxSpace: Optional[int] = None
    network: Optional[str] = None
    io: Optional[str] = None
    networkMode: str = "bridge"
    networkAliases: List[str] = field(default_factory=list)
    cpusetCpus: str = ""
    cpuUsage: int = 100
    workingDir: str = ""
    env: List[str] = field(default_factory=list)


@dataclass
class TerminalOption:
    haveColor: bool = False
    pty: bool = True


@dataclass
class EventTask:
    autoStart: bool = False
    autoRestart: bool = True
    ignore: bool = False


@dataclass
class PingConfig:
    ip: str = ""
    port: int = 25565
    type: int = 1


@dataclass
class InstanceConfig:
    nickname: str = ""
    startCommand: str = ""
    stopCommand: str = ""
    cwd: str = ""
    ie: str = "gbk"  # 输入编码
    oe: str = "gbk"  # 输出编码
    createDatetime: int = 0
    lastDatetime: int = 0
    type: str = "universal"
    tag: List[str] = field(default_factory=list)
    endTime: int = 0
    fileCode: str = "gbk"
    processType: str = ""
    updateCommand: str = ""
    actionCommandList: List[str] = field(default_factory=list)
    crlf: int = 2
    docker: DockerConfig = field(default_factory=DockerConfig)
    enableRcon: bool = True
    rconPassword: str = ""
    rconPort: int = 2557
    rconIp: str = ""
    terminalOption: TerminalOption = field(default_factory=TerminalOption)
    eventTask: EventTask = field(default_factory=EventTask)
    pingConfig: PingConfig = field(default_factory=PingConfig)


@dataclass
class ProcessInfo:
    cpu: int = 0
    memory: int = 0
    ppid: int = 0
    pid: int = 0
    ctime: int = 0
    elapsed: int = 0
    timestamp: int = 0


@dataclass
class InstanceInfo:
    currentPlayers: int = -1
    fileLock: int = 0
    maxPlayers: int = -1
    openFrpStatus: bool = False
    playersChart: List[Dict] = field(default_factory=list)
    version: str = ""


@dataclass
class InstanceDetail:
    config: InstanceConfig = field(default_factory=InstanceConfig)
    info: InstanceInfo = field(default_factory=InstanceInfo)
    instanceUuid: str = ""
    processInfo: ProcessInfo = field(default_factory=ProcessInfo)
    space: int = 0
    started: int = 0  # 启动次数
    status: int = 0  # -1 = 忙碌, 0 = 停止, 1 = 停止中, 2 = 启动中, 3 = 运行中


@dataclass
class InstanceDetailList:
    pageSize: int = 0
    maxPage: int = 0
    data: List[InstanceDetail] = field(default_factory=list)


@dataclass
class UserInstancesList:
    instanceUuid: str = ""
    daemonId: str = ""

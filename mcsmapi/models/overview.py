from pydantic import BaseModel
from mcsmapi.models.common import CpuMemChart, InstanceInfo, ProcessInfo
from mcsmapi.models.daemon import DaemonModel


class SystemUser(BaseModel):
    """系统用户信息"""

    uid: int = 0
    """用户 ID (UID)"""
    gid: int = 0
    """用户组 ID (GID)"""
    username: str = ""
    """用户名"""
    homedir: str = ""
    """用户主目录"""
    shell: str | None = None
    """默认 Shell 解释器"""


class SystemInfo(BaseModel):
    """系统信息"""

    user: SystemUser = SystemUser()
    """当前登录用户信息"""
    time: int = 0
    """系统当前时间 (Unix 时间戳)"""
    totalmem: int = 0
    """系统总内存大小 (单位: 字节)"""
    freemem: int = 0
    """系统空闲内存大小 (单位: 字节)"""
    type: str = ""
    """操作系统类型"""
    version: str = ""
    """操作系统版本"""
    node: str = ""
    """系统节点名称"""
    hostname: str = ""
    """主机名"""
    loadavg: list[float] = []
    """系统负载平均值 (过去 1、5、15 分钟)"""
    platform: str = ""
    """操作系统平台"""
    release: str = ""
    """系统发行版本信息"""
    uptime: float = 0
    """系统运行时间 (单位: 秒)"""
    cpu: float = 0
    """CPU 当前使用率 (单位: %)"""


class RecordInfo(BaseModel):
    """安全记录信息"""

    logined: int = 0
    """成功登录次数"""
    illegalAccess: int = 0
    """非法访问次数"""
    banips: int = 0
    """被封禁的 IP 数量"""
    loginFailed: int = 0
    """登录失败次数"""



class ChartInfo(BaseModel):
    """图表数据信息"""

    system: list[CpuMemChart] = []
    """系统统计信息"""
    request: list[InstanceInfo] = []
    """实例统计信息"""


class RemoteCountInfo(BaseModel):
    """远程守护进程统计信息"""

    total: int = 0
    """远程守护进程总数"""
    available: int = 0
    """可用的远程守护进程数量"""


class OverviewModel(BaseModel):
    """系统概览信息"""

    version: str = ""
    """系统当前版本"""
    specifiedDaemonVersion: str = ""
    """指定的守护进程 (Daemon) 版本"""
    system: SystemInfo = SystemInfo()
    """系统信息"""
    record: RecordInfo = RecordInfo()
    """安全访问记录"""
    process: ProcessInfo = ProcessInfo()
    """进程状态信息"""
    chart: ChartInfo = ChartInfo()
    """系统与请求统计图表数据"""
    remoteCount: RemoteCountInfo = RemoteCountInfo()
    """远程守护进程统计信息"""
    remote: list[DaemonModel] = []
    """远程守护进程详细信息"""

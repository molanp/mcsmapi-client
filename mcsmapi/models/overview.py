from typing import Dict, List, Optional
from pydantic import BaseModel
from mcsmapi.models.daemon import DaemonModel


class SystemUser(BaseModel):
    """系统用户信息"""

    """用户 ID (UID)"""
    uid: int = 0
    """用户组 ID (GID)"""
    gid: int = 0
    """用户名"""
    username: str = ""
    """用户主目录"""
    homedir: str = ""
    """默认 Shell 解释器 (可选)"""
    shell: Optional[str] = None


class SystemInfo(BaseModel):
    """系统信息"""

    """当前登录用户信息"""
    user: SystemUser = SystemUser()
    """系统当前时间 (Unix 时间戳)"""
    time: int = 0
    """系统总内存大小 (单位: 字节)"""
    totalmem: int = 0
    """系统空闲内存大小 (单位: 字节)"""
    freemem: int = 0
    """操作系统类型"""
    type: str = ""
    """操作系统版本"""
    version: str = ""
    """系统节点名称"""
    node: str = ""
    """主机名"""
    hostname: str = ""
    """系统负载平均值 (过去 1、5、15 分钟)"""
    loadavg: List[float] = []
    """操作系统平台"""
    platform: str = ""
    """系统发行版本信息"""
    release: str = ""
    """系统运行时间 (单位: 秒)"""
    uptime: float = 0
    """CPU 当前使用率 (单位: %)"""
    cpu: float = 0


class RecordInfo(BaseModel):
    """安全记录信息"""

    """成功登录次数"""
    logined: int = 0
    """非法访问次数"""
    illegalAccess: int = 0
    """被封禁的 IP 数量"""
    banips: int = 0
    """登录失败次数"""
    loginFailed: int = 0


class ChartInfo(BaseModel):
    """图表数据信息"""

    """系统性能数据 (CPU/内存等)"""
    system: List[Dict[str, float]] = []
    """请求统计信息 (HTTP 请求数等)"""
    request: List[Dict[str, int]] = []


class ProcessInfo(BaseModel):
    """进程信息"""

    """CPU 使用率 (单位: %)"""
    cpu: int = 0
    """进程占用内存 (单位: KB)"""
    memory: int = 0
    """进程当前工作目录"""
    cwd: str = ""


class RemoteCountInfo(BaseModel):
    """远程守护进程统计信息"""

    """远程守护进程总数"""
    total: int = 0
    """可用的远程守护进程数量"""
    available: int = 0


class OverviewModel(BaseModel):
    """系统概览信息"""

    """系统当前版本"""
    version: str = ""
    """指定的守护进程 (Daemon) 版本"""
    specifiedDaemonVersion: str = ""
    """系统信息"""
    system: SystemInfo = SystemInfo()
    """安全访问记录"""
    record: RecordInfo = RecordInfo()
    """进程状态信息"""
    process: ProcessInfo = ProcessInfo()
    """系统与请求统计图表数据"""
    chart: ChartInfo = ChartInfo()
    """远程守护进程统计信息"""
    remoteCount: RemoteCountInfo = RemoteCountInfo()
    """远程守护进程详细信息"""
    remote: List["DaemonModel"] = []

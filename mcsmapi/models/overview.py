from enum import Enum
from typing import Literal
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

    system: list[CpuMemChart]
    """系统统计信息"""
    request: list[InstanceInfo]
    """实例统计信息"""


class RemoteCountInfo(BaseModel):
    """远程守护进程统计信息"""

    total: int
    """远程守护进程总数"""
    available: int
    """可用的远程守护进程数量"""


class OverviewModel(BaseModel):
    """系统概览信息"""

    version: str
    """系统当前版本"""
    specifiedDaemonVersion: str
    """指定的守护进程 (Daemon) 版本"""
    system: SystemInfo
    """系统信息"""
    record: RecordInfo
    """安全访问记录"""
    process: ProcessInfo
    """进程状态信息"""
    chart: ChartInfo
    """系统与请求统计图表数据"""
    remoteCount: RemoteCountInfo
    """远程守护进程统计信息"""
    remote: list[DaemonModel]
    """远程守护进程详细信息"""


class LogType(Enum):
    """操作类型"""

    # 系统相关
    SYSTEM_CONFIG_CHANGE = "system_config_change"

    # 用户相关
    USER_LOGIN = "user_login"
    USER_CONFIG_CHANGE = "user_config_change"
    USER_DELETE = "user_delete"
    USER_CREATE = "user_create"

    # 守护进程相关
    DAEMON_CONFIG_CHANGE = "daemon_config_change"
    DAEMON_REMOVE = "daemon_remove"
    DAEMON_CREATE = "daemon_create"

    # 实例任务相关
    INSTANCE_TASK_DELETE = "instance_task_delete"
    INSTANCE_TASK_CREATE = "instance_task_create"

    # 实例文件相关
    INSTANCE_FILE_DELETE = "instance_file_delete"
    INSTANCE_FILE_DOWNLOAD = "instance_file_download"
    INSTANCE_FILE_UPDATE = "instance_file_update"
    INSTANCE_FILE_UPLOAD = "instance_file_upload"

    # 实例操作相关
    INSTANCE_DELETE = "instance_delete"
    INSTANCE_CREATE = "instance_create"
    INSTANCE_CONFIG_CHANGE = "instance_config_change"
    INSTANCE_KILL = "instance_kill"
    INSTANCE_UPDATE = "instance_update"
    INSTANCE_RESTART = "instance_restart"
    INSTANCE_STOP = "instance_stop"
    INSTANCE_START = "instance_start"


class LogDetail(BaseModel):
    """操作日志详情"""

    operation_id: str
    """操作者uuid"""
    operator_name: str | None = None
    """操作者用户名"""
    operation_time: str
    """操作时间戳"""
    operator_ip: str
    """操作者ip"""
    operation_level: Literal["info", "warning", "error", "unknown"]
    """日志等级"""
    type: LogType
    """操作类型"""
    instance_name: str | None = None
    """实例名称(仅实例事件存在)"""
    instance_id: str | None = None
    """实例ID(仅实例事件存在)"""
    daemon_id: str | None = None
    """守护进程ID(仅实例事件和守护进程事件存在)"""
    login_result: bool | None = None
    """登录结果(仅登录事件存在)"""
    file: str | None = None
    """文件名(仅文件操作事件存在)"""
    task_name: str | None = None
    """任务名称(仅任务操作事件存在)"""

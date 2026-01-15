from typing import Any
from pydantic import BaseModel
from mcsmapi.models.instance import InstanceCreateResult, InstanceDetail
from mcsmapi.models.common import ProcessInfo, InstanceStat, CpuMemChart


class SystemInfo(BaseModel):
    """节点系统信息"""

    type: str
    """系统类型"""
    hostname: str
    """主机名"""
    platform: str
    """平台架构"""
    release: str
    """系统版本"""
    uptime: float
    """系统运行时间(单位: sec)"""
    cwd: str
    """远程节点运行路径"""
    loadavg: tuple[float, float, float]
    """系统负载平均值（仅适用于 Linux 和 macOS），表示过去 **1 分钟、5 分钟、15 分钟** 内的 CPU 负载情况"""
    freemem: int
    """可用内存(单位: byte)"""
    cpuUsage: float
    """cpu使用率"""
    memUsage: float
    """内存使用率"""
    totalmem: int
    """内存总量(单位: byte)"""


class DaemonSetting(BaseModel):
    """节点系统配置信息"""

    language: str
    """节点语言"""
    uploadSpeedRate: int
    """上传速度限制(0为不限制, 限制为(n * 64)KB/s)"""
    downloadSpeedRate: int
    """下载速度限制(0为不限制, 限制为(n * 64)KB/s)"""
    portRangeStart: int
    """端口范围起始值"""
    portRangeEnd: int
    """端口范围结束值"""
    portAssignInterval: int
    """未知"""
    port: int
    """节点监听端口"""
    maxDownloadFromUrlFileCount: int
    """允许同时下载的远程下载任务数量"""


class DaemonOperation(BaseModel):
    uuid: str
    """节点UUID"""

    def delete(self):
        """
        删除该节点

        :returns: 操作成功后返回True
        """
        from mcsmapi.apis.daemon import Daemon

        return Daemon.delete(self.uuid)

    def link(self):
        """
        尝试连接该节点

        :returns: 操作成功后返回True
        """
        from mcsmapi.apis.daemon import Daemon

        return Daemon.link(self.uuid)

    def updateConfig(self, config: dict[str, Any]) -> bool:
        """
        更新该节点的配置

        :params config: 节点的配置信息，以字典形式提供，缺失内容使用原节点配置填充

        :returns: 操作成功后返回True
        """
        from mcsmapi.apis.daemon import Daemon

        updated_config = self.model_dump()
        updated_config.update(config)

        daemon_config = DaemonUpdateConfig(**updated_config).model_dump()

        return Daemon.update(self.uuid, daemon_config)

    def createInstance(self, config: dict[str, Any]) -> InstanceCreateResult:
        """
        在当前节点创建一个实例

        :params config: 实例的配置信息，以字典形式提供，缺失内容由InstanceConfig模型补全

        :returns: 一个包含新创建实例信息的结果对象
        """
        from mcsmapi.apis.instance import Instance
        from .instance import InstanceConfig

        return Instance.create(self.uuid, InstanceConfig(**config).model_dump())

    def deleteInstance(self, uuids: list[str], deleteFile=False) -> list[str]:
        """
        删除当前节点的一个或多个实例

        :params uuids: 要删除的实例UUID列表
        :params deleteFile: 是否删除关联的文件

        :returns: 删除操作后返回的UUID列表
        """
        from mcsmapi.apis.instance import Instance

        return Instance.delete(self.uuid, uuids, deleteFile)


class DaemonConfig(BaseModel):
    """节点配置信息"""

    ip: str = "localhost"
    """远程节点的ip"""
    port: int = 24444
    """远程节点的端口"""
    prefix: str = ""
    """远程节点的路径前缀"""
    remarks: str = "Unnamed Node"
    """远程节点的备注"""
    apiKey: str = ""
    """远程节点的apiKey"""


class DaemonStatus(DaemonOperation):
    """节点状态信息"""

    available: bool
    """节点可用状态"""
    ip: str
    """节点ip"""
    port: int
    """节点端口"""
    prefix: str
    """节点路径前缀"""
    remarks: str
    """节点备注"""


class DaemonSystemInfo(DaemonStatus):
    """节点信息"""

    version: str | None = None
    """节点版本"""
    process: ProcessInfo | None = None
    """节点进程信息"""
    instance: InstanceStat | None = None
    """节点实例统计信息"""
    system: SystemInfo | None = None
    """节点系统信息"""
    cpuMemChart: list[CpuMemChart] | None = None
    """cpu和内存使用趋势"""
    config: DaemonSetting | None = None
    """节点配置信息"""


class DaemonInfo(DaemonStatus):
    """节点信息"""

    instances: list[InstanceDetail]
    """节点实例列表"""


class DaemonUpdateConfig(DaemonConfig):
    """节点更新配置信息"""

    setting: DaemonSetting
    """节点系统配置"""

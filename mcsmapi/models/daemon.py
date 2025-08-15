from typing import Any
from pydantic import BaseModel
from mcsmapi.models.instance import InstanceCreateResult
from mcsmapi.models.common import ProcessInfo, InstanceInfo, CpuMemChart


class SystemInfo(BaseModel):
    """节点系统信息"""

    type: str = ""
    """系统类型"""
    hostname: str = ""
    """主机名"""
    platform: str = ""
    """平台架构"""
    release: str = ""
    """系统版本"""
    uptime: float = 0
    """系统运行时间(单位: sec)"""
    cwd: str = ""
    """远程节点运行路径"""
    loadavg: list[float] = []
    """系统负载平均值（仅适用于 Linux 和 macOS），表示过去 **1 分钟、5 分钟、15 分钟** 内的 CPU 负载情况"""
    freemem: int = 0
    """可用内存(单位: byte)"""
    cpuUsage: float = 0
    """cpu使用率"""
    memUsage: float = 0
    """内存使用率"""
    totalmem: int = 0
    """内存总量(单位: byte)"""
    processCpu: int = 0
    """未知"""
    processMem: int = 0
    """未知"""


class DaemonModel(BaseModel):
    """节点详细信息"""

    version: str = ""
    """远程节点版本"""
    process: ProcessInfo = ProcessInfo()
    """远程节点的基本信息"""
    instance: InstanceInfo = InstanceInfo()
    """远程节点实例基本信息"""
    system: SystemInfo = SystemInfo()
    """远程节点系统信息"""
    cpuMemChart: list[CpuMemChart] = []
    """cpu和内存使用趋势"""
    uuid: str = ""
    """远程节点的uuid"""
    ip: str = ""
    """远程节点的ip"""
    port: int = 24444
    """远程节点的端口"""
    prefix: str = ""
    """远程节点的路径前缀"""
    available: bool = False
    """远程节点的可用状态"""
    remarks: str = ""
    """远程节点的备注"""

    def delete(self) -> bool:
        """
        删除该节点。

        返回:
        - bool: 删除成功后返回True
        """
        from mcsmapi.apis.daemon import Daemon

        return Daemon.delete(self.uuid)

    def link(self) -> bool:
        """
        链接该节点。

        返回:
        - bool: 链接成功后返回True
        """
        from mcsmapi.apis.daemon import Daemon

        return Daemon.link(self.uuid)

    def updateConfig(self, config: dict[str, Any]) -> bool:
        """
        更新该节点的配置。

        参数:
        - config (dict[str, Any]): 节点的配置信息，以字典形式提供，缺失内容使用原节点配置填充。

        返回:
        - bool: 更新成功后返回True
        """
        from mcsmapi.apis.daemon import Daemon

        updated_config = self.model_dump()
        updated_config.update(config)
        # 过滤节点配置中不需要的字段
        daemon_config_dict = {
            key: updated_config[key]
            for key in DaemonConfig.model_fields.keys()
            if key in updated_config
        }

        daemon_config = DaemonConfig(**daemon_config_dict).model_dump()

        return Daemon.update(self.uuid, daemon_config)

    def createInstance(self, config: dict[str, Any]) -> "InstanceCreateResult":
        """
        在当前节点创建一个实例。

        参数:
        - config (dict[str, Any]): 实例的配置信息，以字典形式提供，缺失内容由InstanceConfig模型补全。

        返回:
        - InstanceCreateResult: 一个包含新创建实例信息的结果对象，内容由InstanceCreateResult模型定义。
        """
        from mcsmapi.apis.instance import Instance
        from .instance import InstanceConfig

        return Instance.create(self.uuid, InstanceConfig(**config).dict())

    def deleteInstance(self, uuids: list[str], deleteFile=False) -> list[str]:
        """
        删除当前节点的一个或多个实例。

        参数:
        - uuids (list[str]): 要删除的实例UUID列表。
        - deleteFile (bool, optional): 是否删除关联的文件，默认为False。

        返回:
        - list[str]: 删除操作后返回的UUID列表。
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
    remarks: str = "New Daemon"
    """远程节点的备注"""
    available: bool = True
    """远程节点的可用状态"""

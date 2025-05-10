from typing import Any, List
from pydantic import BaseModel
from mcsmapi.models.instance import InstanceCreateResult


class CpuMemChart(BaseModel):
    cpu: float = 0
    mem: float = 0


class ProcessInfo(BaseModel):
    cpu: int = 0
    memory: int = 0
    cwd: str = ""


class InstanceInfo(BaseModel):
    running: int = 0
    total: int = 0


class SystemInfo(BaseModel):
    type: str = ""
    hostname: str = ""
    platform: str = ""
    release: str = ""
    uptime: float = 0
    cwd: str = ""
    loadavg: List[float] = []
    freemem: int = 0
    cpuUsage: float = 0
    memUsage: float = 0
    totalmem: int = 0
    processCpu: int = 0
    processMem: int = 0


class DaemonModel(BaseModel):
    version: str = ""
    process: ProcessInfo = ProcessInfo()
    instance: InstanceInfo = InstanceInfo()
    system: SystemInfo = SystemInfo()
    cpuMemChart: List[CpuMemChart] = []
    uuid: str = ""
    ip: str = ""
    port: int = 24444
    prefix: str = ""
    available: bool = False
    remarks: str = ""

    def delete(self) -> bool:
        """
        删除该节点。

        返回:
        - bool: 删除成功后返回True
        """
        from mcsmapi.apis.daemon import Daemon

        return Daemon().delete(self.uuid)

    def link(self) -> bool:
        """
        链接该节点。

        返回:
        - bool: 链接成功后返回True
        """
        from mcsmapi.apis.daemon import Daemon

        return Daemon().link(self.uuid)

    def updateConfig(self, config: dict[str, Any]) -> bool:
        """
        更新该节点的配置。

        参数:
        - config (dict[str, Any]): 节点的配置信息，以字典形式提供，缺失内容使用原节点配置填充。

        返回:
        - bool: 更新成功后返回True
        """
        from mcsmapi.apis.daemon import Daemon

        updated_config = self.dict()
        updated_config.update(config)
        # 过滤节点配置中不需要的字段
        daemon_config_dict = {
            key: updated_config[key]
            for key in DaemonConfig.__fields__.keys()
            if key in updated_config
        }

        daemon_config = DaemonConfig(**daemon_config_dict).dict()

        return Daemon().update(self.uuid, daemon_config)

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

        return Instance().create(self.uuid, InstanceConfig(**config).dict())

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

        return Instance().delete(self.uuid, uuids, deleteFile)


class DaemonConfig(BaseModel):
    ip: str = "localhost"
    port: int = 24444
    prefix: str = ""
    remarks: str = "New Daemon"
    available: bool = True

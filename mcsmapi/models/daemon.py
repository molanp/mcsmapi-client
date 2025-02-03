from typing import List
from pydantic import BaseModel


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
    port: str = ""
    prefix: str = ""
    available: bool = False
    remarks: str = ""


    def delete(self) -> bool:
        """
        删除该节点。

        返回:
        - bool: 删除成功后返回True
        """
        from ..apis.daemon import Daemon

        return Daemon().delete(self.uuid)

    def link(self) -> bool:
        """
        链接该节点。

        返回:
        - bool: 链接成功后返回True
        """
        from ..apis.daemon import Daemon

        return Daemon().link(self.uuid)

    def updateConfig(self, config: dict) -> bool:
        """
        更新该节点的配置。

        参数:
        - config (dict): 节点的配置信息，以字典形式提供，缺失内容由DaemonConfig模型补全。

        返回:
        - bool: 更新成功后返回True
        """
        from ..apis.daemon import Daemon

        return Daemon().update(self.uuid, config)


class DaemonConfig(BaseModel):
    ip: str = "localhost"
    port: int = 24444
    prefix: str = ""
    remarks: str = "New Daemon"
    available: bool = True

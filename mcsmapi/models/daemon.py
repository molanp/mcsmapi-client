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

class DaemonConfig(BaseModel):
    ip: str = "localhost"
    port: int = 24444
    prefix: str = ""
    remarks: str = "New Daemon"
    available: bool = True

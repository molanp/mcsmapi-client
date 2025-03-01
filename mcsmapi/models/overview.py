from typing import Dict, List, Optional
from pydantic import BaseModel
from mcsmapi.models.daemon import DaemonModel


class SystemUser(BaseModel):
    uid: int = 0
    gid: int = 0
    username: str = ""
    homedir: str = ""
    shell: Optional[str] = None


class SystemInfo(BaseModel):
    user: SystemUser = SystemUser()
    time: int = 0
    totalmem: int = 0
    freemem: int = 0
    type: str = ""
    version: str = ""
    node: str = ""
    hostname: str = ""
    loadavg: List[float] = []
    platform: str = ""
    release: str = ""
    uptime: float = 0
    cpu: float = 0



class RecordInfo(BaseModel):
    logined: int = 0
    illegalAccess: int = 0
    banips: int = 0
    loginFailed: int = 0


class ChartInfo(BaseModel):
    system: List[Dict[str, float]] = []
    request: List[Dict[str, int]] = []


class ProcessInfo(BaseModel):
    cpu: int = 0
    memory: int = 0
    cwd: str = ""


class RemoteCountInfo(BaseModel):
    total: int = 0
    available: int = 0


class OverviewModel(BaseModel):
    version: str = ""
    specifiedDaemonVersion: str = ""
    system: SystemInfo = SystemInfo()
    record: RecordInfo = RecordInfo()
    process: ProcessInfo = ProcessInfo()
    chart: ChartInfo = ChartInfo()
    remoteCount: RemoteCountInfo = RemoteCountInfo()
    remote: List["DaemonModel"] = []


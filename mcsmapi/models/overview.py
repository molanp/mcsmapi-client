from dataclasses import dataclass
from typing import Any, Dict, List
from mcsmapi.apis.daemon import Daemon

@dataclass
class SystemInfo:
    type: str
    version: str
    platform: str

@dataclass
class RecordInfo:
    logined: int
    loginFailed: int
    banips: List[str]
    illegalAccess: int

@dataclass
class ProcessInfo:
    cpuUsage: float
    memoryUsage: float
    cwd: str

@dataclass
class RemoteCountInfo:
    total: int
    available: int

class OverviewModel:
    def __init__(self, raw_data: Dict[str, Any]):
        """
        Initialize the Overview class with raw data.

        :param raw_data: A dictionary containing the raw data.
        """
        try:
            self.raw = raw_data
            self.version = raw_data["version"]
            self.specifiedDaemonVersion = raw_data["specifiedDaemonVersion"]
            self.system = SystemInfo(**raw_data["system"])
            self.record = RecordInfo(**raw_data["record"])
            self.process = ProcessInfo(**raw_data["process"])
            self.chart = raw_data["chart"]
            self.remoteCount = RemoteCountInfo(**raw_data["remoteCount"])
            self.remoteList = Daemon(raw_data["remote"])
        except KeyError as e:
            raise ValueError(f"Missing key in raw_data: {e}") from e
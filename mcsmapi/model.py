from .APIs.Daemon import Daemon


class Overview:
    def __init__(self, raw_data):
        self.raw = raw_data
        self.version = raw_data["version"]
        self.specifiedDaemonVersion = raw_data["specifiedDaemonVersion"]
        self.system = self.SystemInfo(raw_data["system"])
        self.record = self.RecordInfo(raw_data["record"])
        self.process = raw_data["process"]
        self.chart = raw_data["chart"]
        self.remoteCount = raw_data["remoteCount"]
        self.remoteList = Daemon(raw_data["remote"])

    class SystemInfo:
        def __init__(self, system_data):
            self.type = system_data["type"]
            self.version = system_data["version"]
            self.platform = system_data["platform"]

    class RecordInfo:
        def __init__(self, raw_data):
            self.logined = raw_data["logined"]
            self.loginFailed = raw_data["loginFailed"]
            self.banips = raw_data["banips"]
            self.illegalAccess = raw_data["illegalAccess"]

    class ProcessInfo:
        def __init__(self, raw_data):
            self.cpu = raw_data["cpu"]
            self.memory = raw_data["memory"]
            self.cwd = raw_data["cwd"]

    class RemoteCountInfo:
        def __init__(self, raw_data):
            self.total = raw_data["total"]
            self.available = raw_data["available"]


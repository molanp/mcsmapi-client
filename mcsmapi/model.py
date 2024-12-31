from .APIs.Daemon import Daemon

class SystemInfo:
    def __init__(self, system_data):
        self.type = system_data['type']
        self.version = system_data['version']
        self.platform = system_data['platform']


class Overview:
    def __init__(self, raw_data):
        self.raw = raw_data
        self.version = raw_data['version']
        self.specifiedDaemonVersion = raw_data['specifiedDaemonVersion']
        self.system = SystemInfo(raw_data['system'])
        self.record = raw_data['record']
        self.process = raw_data['process']
        self.chart = raw_data['chart']
        self.remoteCount = raw_data['remoteCount']
        self.remoteList =Daemon( raw_data['remote'])

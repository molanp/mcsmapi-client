import unittest
from pydantic import ValidationError
from mcsmapi.models.overview import OverviewModel


class TestOverviewModel(unittest.TestCase):
    def setUp(self):
        self.valid_overview_model_dict = {
            "version": "10.2.1",
            "specifiedDaemonVersion": "4.4.1",
            "process": {
                "cpu": 0,
                "memory": 219439104,
                "cwd": "Z:\\Workspace\\MCSManager\\panel",
            },
            "record": {"logined": 2, "illegalAccess": 2, "banips": 0, "loginFailed": 0},
            "system": {
                "user": {
                    "uid": -1,
                    "gid": -1,
                    "username": "MCSManager",
                    "homedir": "X:\\Users\\MCSManager",
                    "shell": None,
                },
                "time": 1718594177859,
                "totalmem": 16577519520,
                "freemem": 10966386688,
                "type": "Windows_NT",
                "version": "Windows 10 Pro for Workstations",
                "node": "v17.9.1",
                "hostname": "MCSManager-Workstation",
                "loadavg": [0, 0, 0],
                "platform": "win32",
                "release": "10.0.22631",
                "uptime": 905020.0,
                "cpu": 0.11684482123110951,
            },
            "chart": {
                "system": [{"cpu": 8.1, "mem": 64.5}],
                "request": [{"value": 6, "totalInstance": 23, "runningInstance": 3}],
            },
            "remoteCount": {"available": 3, "total": 3},
            "remote": [
                {
                    "version": "3.4.0",
                    "process": {
                        "cpu": 3550442695,
                        "memory": 22620272,
                        "cwd": "/opt/mcsmanager/daemon",
                    },
                    "instance": {"running": 0, "total": 6},
                    "system": {
                        "type": "Linux",
                        "hostname": "NYA-Dev-01",
                        "platform": "linux",
                        "release": "5.15.0-101-generic",
                        "uptime": 39.63,
                        "cwd": "/opt/mcsmanager/daemon",
                        "loadavg": [3.5, 0.85, 0.28],
                        "freemem": 7254478848,
                        "cpuUsage": 0.002512562814070307,
                        "memUsage": 0.12453628345617548,
                        "totalmem": 8286441472,
                        "processCpu": 0,
                        "processMem": 0,
                    },
                    "cpuMemChart": [{"cpu": 0, "mem": 13}],
                    "uuid": "957c6bddf379445c82bac5edf7684bbc",
                    "ip": "s1.example.com",
                    "port": 24444,
                    "prefix": "",
                    "available": True,
                    "remarks": "CN-ZJ-DEV-01",
                }
            ],
        }

    def test_valid_overview_model_from_dict(self):
        overview_model = OverviewModel(**self.valid_overview_model_dict)
        self.assertEqual(overview_model.version, "10.2.1")
        self.assertEqual(overview_model.specifiedDaemonVersion, "4.4.1")
        self.assertEqual(overview_model.system.user.username, "MCSManager")
        self.assertEqual(overview_model.record.logined, 2)
        self.assertEqual(overview_model.process.cpu, 0)
        self.assertIsInstance(overview_model.chart.request, list)
        self.assertEqual(overview_model.remoteCount.total, 3)
        self.assertEqual(overview_model.remote[0].remarks, "CN-ZJ-DEV-01")

    def test_invalid_overview_model_from_dict(self):
        invalid_overview_model_dict = self.valid_overview_model_dict.copy()
        invalid_overview_model_dict["chart"] = []  # Invalid type for chart
        with self.assertRaises(ValidationError):
            OverviewModel(**invalid_overview_model_dict)


if __name__ == "__main__":
    unittest.main()

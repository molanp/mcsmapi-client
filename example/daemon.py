from mcsmapi import MCSMAPI
from mcsmapi.models.daemon import DaemonConfig

mcsm = MCSMAPI("http://localhost:23333")

mcsm.login("admin", "547cABC9bf88@")

# mcsm.login_with_apikey("apikey")

daemon_object = mcsm.daemon

# show Daemon list

print(daemon_object.config())

# 创建节点
daemonId = daemon_object.add(
    DaemonConfig(
        ip="localhost",
        port=24444,
        prefix="",
        remarks="Unnamed Node",
    )
)
# 删除节点
daemon_object.delete(daemonId)

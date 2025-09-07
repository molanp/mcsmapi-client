from mcsmapi import MCSMAPI

mcsm = MCSMAPI("http://localhost:23333")

mcsm.login("admin", "547cABC9bf88@")

# mcsm.login_with_apikey("apikey")

daemon_object = mcsm.daemon()

# show Daemon list

print(daemon_object.config())

# 创建节点
daemonId = daemon_object.add(
    {
        "ip": "localhost",
        "port": 24444,
        "prefix": "",
        "remarks": "Unnamed Node",
        "available": True,
    }
)
# 删除节点
daemon_object.delete(daemonId)

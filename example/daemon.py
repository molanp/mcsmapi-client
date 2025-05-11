from mcsmapi import MCSMAPI

mcsm = MCSMAPI("http://localhost:23333")

mcsm.login("admin", "547cABC9bf88@")

# mcsm.login_with_apikey("apikey")

daemon_object = mcsm.daemon()

# show Daemon list

print(daemon_object.show())

# 创建节点
daemonId = daemon_object.add(
    {
        "ip": "localhost",
        "port": 24444,
        "prefix": "",
        "remarks": "New Daemon",
        "available": True,
    }
)
# 删除节点
daemon_object.delete(daemonId)

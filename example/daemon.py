from mcsmapi import MCSMAPI

mcsm = MCSMAPI("http://localhost:23333")

mcsm.login("admin", "547cABC9bf88@")

# mcsm.login_with_apikey("apikey")

daemonM = mcsm.daemon()

# 创建节点
daemonId = daemonM.add(
    {
        "ip": "localhost",
        "port": 24444,
        "prefix": "",
        "remarks": "New Daemon",
        "available": True,
    }
)
# 删除节点
daemonM.delete(daemonId)

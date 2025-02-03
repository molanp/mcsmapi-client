from mcsmapi import MCSMAPI

mcsm = MCSMAPI("http://localhost:23333")

mcsm.login("admin", "547cABC9bf88@")

# mcsm.login_with_apikey("apikey")

# Get dashboard data
overview = mcsm.overview()

mcsm_version = mcsm.overview().version

remotes = overview.remote

for remote in remotes:
    print(remote.remarks)
    print(remote.ip)
    print(remote.port)
    print(remote.prefix)
    print(remote.available)
    print(remote.version)
    print(remote.process.cpu)
    print(remote.system.freemem)
    print(remote.system.hostname)
    print(remote.system.loadavg)


remote = remotes[0]

# Connect to the remote
remote.link()

# Delete the instance in the daemon
remote.deleteInstance(["uuid1", "uuid2"], True)

# Update the daemon config
remote.updateConfig({"prefix": "", "remarks": "This is daemon name"})

# Delete the daemon
remote.delete()

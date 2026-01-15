from mcsmapi import MCSMAPI

mcsm = MCSMAPI("http://localhost:23333")

mcsm.login("admin", "547cABC9bf88@")

# mcsm.login_with_apikey("apikey")

# Get dashboard data
overview = mcsm.overview
overview_data = overview.overview()

mcsm_version = overview_data.version

remotes = overview_data.remote

for remote in remotes:
    print(remote.remarks)
    print(remote.ip)
    print(remote.port)
    print(remote.prefix)
    if remote.available:
        print(remote.version)
        print(remote.process.cpu) # type: ignore
        print(remote.system.freemem) # type: ignore
        print(remote.system.hostname) # type: ignore
        print(remote.system.loadavg) # type: ignore
    else:
        print("Not available")


remote = remotes[0]

# Connect to the remote
remote.link()

# Delete the instance in the daemon
remote.deleteInstance(["uuid1", "uuid2"], True)

# Update the daemon config
remote.updateConfig({"prefix": "", "remarks": "This is daemon name"})

# Delete the daemon
remote.delete()

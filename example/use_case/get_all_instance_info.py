from mcsmapi import MCSMAPI
import json

baseurl = "http://localhost:23333" # Change to your MCSM panel address and port(include http or https etc.).

mcsm = MCSMAPI(baseurl)

# Password login
address = "admin" # Please change to your MCSM panel username.
password = "547cABC9bf88@" # Please change to your MCSM panel password.
mcsm.login(address, password)

# Api login
#apikey = "apikey" # Please change to your MCSM panel apikey.
#mcsm.login_with_apikey(apikey)

# Get all instance info
def get_all_instance_info(daemon_id: str):
    # Get all instance info from the daemon
    instance_object = mcsm.instance
    instance_list = instance_object.search(daemonId=daemon_id).data

    return {
        instance.instanceUuid: {
            "name": instance.config.nickname,
            "status": instance.status,
            "daemonId": instance.daemonId,
            "uuid": instance.instanceUuid,
        }
        for instance in instance_list
    }

# Example usage
daemon_id = "your_daemon_id" # Please change to your MCSM panel daemon id.
instance_info = get_all_instance_info(daemon_id)

# Print instance info
print(json.dumps(instance_info, indent=4))

# Optional: Save info to a file in the current directory
with open("instance_info.json", "w") as f:
    content = json.dump(instance_info, f, indent=4)

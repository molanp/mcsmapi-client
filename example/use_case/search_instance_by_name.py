from mcsmapi import MCSMAPI

baseurl = "http://localhost:23333" # Change to your MCSM panel address and port(include http or https etc.).

mcsm = MCSMAPI(baseurl)

# Password login
#address = "admin" # Please change to your MCSM panel username.
#password = "547cABC9bf88@" # Please change to your MCSM panel password.
#mcsm.login(address, password)

# Api login
apikey = "apikey" # Please change to your MCSM panel apikey.
mcsm.login_with_apikey(apikey)

# Get instance 
def get_instance(daemon_id: str, instance_name: str):
    # Get specific instance info from the daemon by name
    instance_object = mcsm.instance
    instance_list = instance_object.search(daemonId=daemon_id, instance_name=instance_name).data
    
    # Error handling
    if len(instance_list) == 0:
        raise ValueError(f"No instance found with name: {instance_name}")
    elif len(instance_list) > 1:
        error_msg = f"Multiple instances found with name: {instance_name}\n"
        for instance in instance_list:
            error_msg += f"Instance UUID: {instance.instanceUuid}, Status: {instance.status}\n"
        raise ValueError(error_msg)
    
    return instance_list[0]

# Example usage
daemon_id = "your_daemon_id" # Please change to your MCSM panel daemon id.

# Instance name, could be a partial name or empty string to match all instances
instance_name = "your_instance_name" # Please change to your MCSM panel instance name.
instance = get_instance(daemon_id, instance_name)

# Print instance status
print(instance.config.nickname)
print(instance.status)

# Optional:
# start
instance.start()

# stop
instance.stop()

# restart
instance.restart()

# kill
instance.kill()

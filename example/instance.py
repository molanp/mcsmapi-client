from mcsmapi import MCSMAPI

api = MCSMAPI("http://localhost:23333")

api.login("admin", "547cABC9bf88@")

instance_object = api.instance

instance_list = instance_object.search("xxx")

instance = instance_list.data[0]

# start
instance.start()

# stop
instance.stop()

# restart
instance.restart()

# kill
instance.kill()

# show files
file_list = instance.files("", 1, 20)

# show total files
print(file_list.total)

# show file list
fs = file_list.items

f = fs[0]

# rename file
f.rename("new_name")

# copy file
f.copy_to("new_path")
# move file
f.move("new_path")


# delete file
f.delete()


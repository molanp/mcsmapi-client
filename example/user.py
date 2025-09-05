from mcsmapi import MCSMAPI

api = MCSMAPI("http://localhost:23333")

api.login("admin", "547cABC9bf88@")

userManager = api.user()

users = userManager.search()

for user in users.data:
    # 打印所有用户的用户名
    print(user.userName)

# 查找第一个管理员账号
user = api.user().search(role=10).data[0]

# 封禁管理员账号
user.update({"permission": -1})

# 删除管理员账号
user.delete()

# 创建新用户
uuid = userManager.create("test", "54ABCd9bf#").uuid

print("New user uuid:", uuid)

# 删除新用户
userManager.delete([uuid])
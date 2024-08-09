from .common import ApiClient 

class Users:
	def __init__(self, url, apikey=""):
		self.client = ApiClient(url, apikey)
	
	def get_list(self, userName="", page=1, page_size=10, role="") -> dict:
		r = self.client.send("GET", "auth/search", params={"userName": userName, "page": page, "page_size": page_size, "role": role})
		return r
	
	def create(self, username, password, permission=1) -> dict:
		r = self.client.send("POST", "auth", data={"username": username,"password": password,"permission": permission})
		return r
		
	def update(self, uuid, config={}) -> dict:
		r = self.client.send("PUT", "auth", data={"uuid": uuid, "config": config})
		return r
	
	def delete(self, uuids=[]) -> dict:
		r = self.client.send("DELETE", "auth", data=uuids)
		return r

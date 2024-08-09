from .common import ApiClient 

class Instance:
	def __init__(self, url, apikey=""):
		self.client = ApiClient(url, apikey)
	
	def get_list(self, daemonId, page=1,page_size=10,instance_name="", status="") -> dict:
		r = self.client.send("GET","service/remote_service_instances", params={"daemonId": daemonId,"page": page,"page_size": page_size,"instance_name": instance_name,"status": status})
		return r
		
	def detail(self, uuid, daemonId) -> dict:
		r = self.client.send("GET", "instance ", params={"uuid":uuid,"daemonId":daemonId})
		return r
	
	def create(self, daemonId, config) -> dict:
		r = self.client.send("POST", "instance", params ={"daemonId": daemonId}, data=config)
		return r

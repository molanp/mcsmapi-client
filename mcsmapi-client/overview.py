from .common import ApiClient

class Overview:
	def __init__(self, url, apikey=""):
		self.client = ApiClient(url, apikey)
	
	def get_data(self) -> dict :
		r = self.client.send("GET", "overview")
		return r

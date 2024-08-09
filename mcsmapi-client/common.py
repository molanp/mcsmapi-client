import requests

class ApiClient:
	def __init__(self, url, apikey, timeout=5):
		self.url = url
		self.apikey = apikey
		self.timeout = timeout
		
	def send(self, method, endpoint, params=None, data=None) -> dict:
		url = f"{self.url}/api/{endpoint}"
		
		if params is None:
			params = {}
		params['apikey'] = self.apikey
		
		response = requests.request(method, url, params=params, json=data, timeout=self.timeout)
		response.raise_for_status() 
		return response.json()

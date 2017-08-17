
class Page:
	"""docstring for Page"""
	def __init__(self, url):
		self.url = ""
		self.targets = []
		self.hash = ""
		self.content = ""


	def getURL(self):
		return self.url

	
	def getHash(self):
		return self.hash

	def getLinks(self):
		return self.targets

	def getContent(self):
		return self.content
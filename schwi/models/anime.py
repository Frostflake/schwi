import json

class Anime():
	def __init__(name):
		self.id = 0
		self.name = name
		self.year = None
		self.status = "Plan to Watch"
		self.score = None
		self.progress = None
		self.episodecount = None
		self.startdate = None
		self.enddate = None
		self.rewatchcont = 0
		self.notes = ""
		self.externals = {}
		
	def Json():
		return ""
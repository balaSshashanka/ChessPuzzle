import GameConfig

class ObstacleLocation(object):
	def __init__(self,room,floor,Otype):
		self.room = room
		self.floor = floor
		self.Otype = Otype
	def getObstacle(self):
		return self.Otype
	def getRoom(self):
		return self.room
	def getFloor(self):
		return self.floor
import GameConfig

class ObstacleLocation(object):
	def __init__(self,room,floor,Otype):
		self.room = room
		self.floor = floor
		self.Otype = Otype
	def getObstacle(self):
		return Otype
	def getRoom(self):
		return room
	def getFloor(self):
		return floor
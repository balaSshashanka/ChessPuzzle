import GameConfig
from ObstacleLocation import ObstacleLocation

class Building(object):
	def __SetObstacleType(self,location):
		self.Building[location.getFloor()][location.getRoom()] = location.GetObstacle()
	def __init__(self):
		pass
	def __init__(self,location):
		self.BuildingMap = [[GameConfig.ObstacleType.NONE for j in range(GameConfig.constants.COLUMNS)] for i in range(GameConfig.constants.ROWS)]
		for i in range(len(location)):
			__SetObstacleType(location[i])
	def GetObstacleType(self,room,floor):
		return self.Building[room][floor]
	def isValidMove(self,currentPostion,nextPosition):
		if currentPostion.getRow() < Gameconfig.constants.ROWS and 	nextPosition.getRow() < Gameconfig.constants.ROWS and currentPostion.getColumn() < Gameconfig.constants.COLUMNS and 	nextPosition.getColumn() < Gameconfig.constants.COLUMNS:
			rowDif = abs(currentPostion.getRow() - nextPosition.getRow())
			columnDiff = abs(currentPostion.getColumn() - nextPosition.getColumn())

			if (rowDif == 1 and columnDiff == 2) or (rowDif == 2 and columnDiff == 1):
				return True
		return False
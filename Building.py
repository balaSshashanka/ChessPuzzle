import GameConfig
from ObstacleLocation import ObstacleLocation

class Building(object):
	def __SetObstacleType(self,location):
		self.BuildingMap[location.getFloor()][location.getRoom()] = location.getObstacle()
	def __init__(self):
		pass
	def __init__(self,location):
		self.BuildingMap = [[GameConfig.ObstacleType.NONE for j in range(GameConfig.constants.COLUMNS)] for i in range(GameConfig.constants.ROWS)]
		for i in range(len(location)):
			self.__SetObstacleType(location[i])
	def GetObstacleType(self,room,floor):
		return self.BuildingMap[room][floor]
	def isValidMove(self,currentPostion,nextPosition):
		if((currentPostion.GetRow() < GameConfig.constants.ROWS) and (nextPosition.GetRow() < GameConfig.constants.ROWS) and (currentPostion.GetColumn() < GameConfig.constants.COLUMNS) and (nextPosition.GetColumn() < GameConfig.constants.COLUMNS)):
			rowDif = abs(currentPostion.GetRow() - nextPosition.GetRow())
			columnDiff = abs(currentPostion.GetColumn() - nextPosition.GetColumn())
			if (rowDif == 1 and columnDiff == 2) or (rowDif == 2 and columnDiff == 1):
				return True
		return False
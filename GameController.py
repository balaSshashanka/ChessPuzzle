import numpy
from Building import Building
from ObstacleLocation import ObstacleLocation
from Move import Move
from UserBot import UserBot
from GameConfig import GameConfig

class GameController(object):
	def __init__(self):
		__initializeBuilding(self)
	def __MarkPos(self,Path,Location):
		if(Location.getObstacle() == GameConfig.constants.RADAR):
			__MarkRow(self,Path,Location.getFloor())
			__MarkColumn(self,Path,Location.getRoom())
			__MarkDiagonal(self,Path,Location.getFloor(),Location.getRoom())
		elif(Location.getObstacle() == GameConfig.constants.MISSILE):
			__MarkDiagonal(self,Path,Location.getFloor(),Location.getRoom())
		else:
			__MarkRow(self,Path,Location.getFloor())
			__MarkColumn(self,Path,Location.getRoom())
	def __MarkRow(self,Path,row):
		for j in range(GameConfig.constants.COLUMNS):
			Path[row][j] = -1
	def __MarkColumn(self,Path,column):
		for i in range(GameConfig.constants.ROWS):
			Path[i][column] = -1
	def __MarkDiagonal(self,Path,row,column):
		colInc = column + 1
		rowInc = row

		for i in range(row-1 , -1 , -1):
			if colInc < GameConfig.constants.COLUMNS:
				Path[i][colInc] = -1
				colInc = colInc + 1
		colInc = column - 1
		for i in range(row-1 , -1 , -1):
			if colInc > 0:
				Path[i][colInc] = -1
				colInc = colInc - 1
		colInc = column + 1
		for i in range(GameConfig.constants.ROWS):
			if colInc < GameConfig.constants.COLUMNS:
				Path[i][colInc] = -1
				colInc = colInc + 1 
		colInc = column - 1
		for i in range(GameConfig.constants.ROWS):
			if colInc > 0:
				Path[i][colInc] = -1
				colInc = colInc - 1
	def LoadObstaclePosition():
		obstacle = []
		obstacle.append(ObstacleLocation(2,2,GameConfig.ObstacleType.ENEMY_COMMANDER))
		obstacle.append(ObstacleLocation(0,8,GameConfig.ObstacleType.TANK))
		obstacle.append(ObstacleLocation(5,3,GameConfig.ObstacleType.MISSILE))
		obstacle.append(ObstacleLocation(7,9,GameConfig.ObstacleType.HEROBOT))
		obstacle.append(ObstacleLocation(8,1,GameConfig.ObstacleType.RADAR))
		return obstacle
	def __initializeBuilding(self):
		self.locations = LoadObstaclePosition()
		self.BuildingMap = Building(locations)
	def Simulate(self,User):
		origin = ObstacleLocation(0,0,GameConfig.ObstacleType.HEROBOT)
		destination = ObstacleLocation(0,0,GameConfig.ObstacleType.ENEMY_COMMANDER)
		moves = [Move() for j in range(50)]
		Path = numpy.zeros((GameConfig.constants.ROWS,GameConfig.constants.COLUMNS),dtype = int)
		User.MakeMoves(self.BuildingMap,moves,50)
		for i in range(GameConfig.constants.ROWS):
			for j in range(GameConfig.constants.COLUMNS):
				if(BuildingMap.GetObstacleType(i,j) == GameConfig.ObstacleType.HEROBOT):
					location = ObstacleLocation(i,j,GameConfig.ObstacleType.HEROBOT)
					origin = location
				elif(BuildingMap.GetObstacleType(i,j) == GameConfig.ObstacleType.MISSILE):
					location = ObstacleLocation(i,j,GameConfig.ObstacleType.MISSILE)
					__MarkPos(Path,location)
				elif(BuildingMap.GetObstacleType(i,j) == GameConfig.ObstacleType.RADAR):
					location = ObstacleLocation(i,j,GameConfig.ObstacleType.RADAR)
					__MarkPos(Path,location)
				elif(BuildingMap.GetObstacleType(i,j) == GameConfig.ObstacleType.TANK):
					location = ObstacleLocation(i,j,GameConfig.ObstacleType.TANK)
					__MarkPos(Path,location)
				elif(BuildingMap.GetObstacleType(i,j) == GameConfig.ObstacleType.ENEMY_COMMANDER):
					location = ObstacleLocation(i,j,GameConfig.ObstacleType.ENEMY_COMMANDER)
					destination = location
		PrevMove = Move(origin.getFloor(),origin.getRoom())
		for i in range(50):
			if(!((moves[i].GetRow()==dest.GetFloor())and moves[i].GetColumn()==dest.GetRoom())):
				if( BuildingMap.IsValidMove(*PrevMove,moves[i]) and (moves[i].GetRow()!=-1 and moves[i].GetColumn()!=-1)):
					PrevMove = moves[i]
					continue
				else:
					return False
			if(BuildingMap.IsValidMove(*PrevMove,moves[i])):
				return True
		'''
		print(Path)
		for i in range(GameConfig.constants.ROWS):
			for j in range(GameConfig.constants.COLUMNS):
				print(BuildingMap.GetObstacleType(i,j) , end="")
		'''
import numpy
from Building import Building
from ObstacleLocation import ObstacleLocation
from Move import Move
from UserBot import UserBot
import GameConfig

class GameController(object):
	def __init__(self):
		self.__initializeBuilding()
	def __MarkPos(self,Path,Location):
		if(Location.getObstacle() == GameConfig.ObstacleType.RADAR):
			self.__MarkRow(Path,Location.getFloor())
			self.__MarkColumn(Path,Location.getRoom())
			self.__MarkDiagonal(Path,Location.getFloor(),Location.getRoom())
		elif(Location.getObstacle() == GameConfig.ObstacleType.MISSILE):
			self.__MarkDiagonal(Path,Location.getFloor(),Location.getRoom())
		else:
			self.__MarkRow(Path,Location.getFloor())
			self.__MarkColumn(Path,Location.getRoom())
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
	def LoadObstaclePosition(self):
		obstacle = []
		obstacle.append(ObstacleLocation(2,2,GameConfig.ObstacleType.ENEMY_COMMANDER))
		obstacle.append(ObstacleLocation(0,8,GameConfig.ObstacleType.TANK))
		obstacle.append(ObstacleLocation(5,3,GameConfig.ObstacleType.MISSILE))
		obstacle.append(ObstacleLocation(7,9,GameConfig.ObstacleType.HEROBOT))
		obstacle.append(ObstacleLocation(8,1,GameConfig.ObstacleType.RADAR))
		return obstacle
	def __initializeBuilding(self):
		self.locations = self.LoadObstaclePosition()
		self.BuildingMap = Building(self.locations)
	def Simulate(self,User):
		origin = ObstacleLocation(0,0,GameConfig.ObstacleType.HEROBOT)
		destination = ObstacleLocation(0,0,GameConfig.ObstacleType.ENEMY_COMMANDER)
		moves = [Move(0,0) for j in range(50)]
		Path = numpy.zeros((GameConfig.constants.ROWS,GameConfig.constants.COLUMNS),dtype = int)
		User.MakeMoves(self.BuildingMap,moves,50)
		for i in range(GameConfig.constants.ROWS):
			for j in range(GameConfig.constants.COLUMNS):
				if(self.BuildingMap.GetObstacleType(i,j) == GameConfig.ObstacleType.HEROBOT):
					location = ObstacleLocation(i,j,GameConfig.ObstacleType.HEROBOT)
					origin = location
				elif(self.BuildingMap.GetObstacleType(i,j) == GameConfig.ObstacleType.MISSILE):
					location = ObstacleLocation(i,j,GameConfig.ObstacleType.MISSILE)
					self.__MarkPos(Path,location)
				elif(self.BuildingMap.GetObstacleType(i,j) == GameConfig.ObstacleType.RADAR):
					location = ObstacleLocation(i,j,GameConfig.ObstacleType.RADAR)
					self.__MarkPos(Path,location)
				elif(self.BuildingMap.GetObstacleType(i,j) == GameConfig.ObstacleType.TANK):
					location = ObstacleLocation(i,j,GameConfig.ObstacleType.TANK)
					self.__MarkPos(Path,location)
				elif(self.BuildingMap.GetObstacleType(i,j) == GameConfig.ObstacleType.ENEMY_COMMANDER):
					location = ObstacleLocation(i,j,GameConfig.ObstacleType.ENEMY_COMMANDER)
					destination = location
		PrevMove = Move(origin.getFloor(),origin.getRoom())
		for i in range(50):
			if(moves[i].GetRow() != destination.getFloor()):
				if((moves[i].GetColumn() != destination.getRoom())):
					if(self.BuildingMap.isValidMove(PrevMove,moves[i]) and (moves[i].GetRow()!=-1 and moves[i].GetColumn()!=-1)):
						PrevMove = moves[i]
						continue
					else:
						#self.PrintPath(Path)
						return False
			if(BuildingMap.isValidMove(PrevMove,moves[i])):
				#self.PrintPath()
				return True

	def PrintPath(self,Path):
		print(Path)
		for i in range(GameConfig.constants.ROWS):
			for j in range(GameConfig.constants.COLUMNS):
				print(self.BuildingMap.GetObstacleType(i,j))
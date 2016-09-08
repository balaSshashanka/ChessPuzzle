from Building import Building
from Move import Move

class UserBot(object):
	
	def MakeMoves(self,BuildingPlan,moves,num):
		moves[0] = Move(6,7)
		moves[1] = Move(5,5)
		moves[2] = Move(4,3)
		moves[3] = Move(2,2)
		return moves
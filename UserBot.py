from Building import Building
from Move import Move

class UserBot(object):
	
	def MakeMoves(self,BuildingPlan,moves):
		moves[0] = Move(0,1)
		moves[1] = Move(1,3)
		moves[2] = Move(4,5)
		moves[3] = MOve(2,5)
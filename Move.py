class Move(object):

	__room = 0
	__floor = 0

	def __init__(self):
		self.__init__(0,0)
	
	def __init__(self,room,floor):
		self.__room = room
		self.__floor = floor

	def setRow(self,row):
		self.__room = room

	def setColumn(self,column):
		self.__floor

	def GetRow(self):
		return self.__room

	def GetColumn(self):
		return self.__floor
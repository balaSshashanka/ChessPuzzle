from GameController import GameController
from UserBot import UserBot

userBot = UserBot()
gameC = GameController()
returnValue = gameC.Simulate(userBot)
if(returnValue == True):
	print("Enemy Commander defeated")
else:
	print("User defeated")
from GameController import GameController
from UserBot import UserBot
import json

userBot = UserBot()
gameC = GameController()
returnValue = gameC.Simulate(userBot)
'''if(returnValue == True):
	print("Enemy Commander defeated")
else:
	print("User defeated")'''

out = gameC.move
js = json.dumps(out,sort_keys=True)

print(js)
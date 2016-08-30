from collections import namedtuple
from enum import Enum

Constants = namedtuple('Constants',['ROWS','COLUMNS']);
constants = Constants(10,10)

class ObstacleType(Enum):
	NONE = 0
	HEROBOT = 1
	RADAR = 2
	MISSILE = 3
	TANK = 4
	ENEMY_COMMANDER = 5
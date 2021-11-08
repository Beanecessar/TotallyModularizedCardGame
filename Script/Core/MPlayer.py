from Script.Core.MHand import MHand
from Script.Core.MGrave import MGrave

class Wind(object):
	Invalid = 0
	East = 1
	South = 2
	West = 3
	North = 4

class MPlayer(object):
	def __init__(self) -> None:
		super().__init__()
		self.hand = MHand()
		self.grave = MGrave()
		self.points = 0
		self.pos = Wind.Invalid
		self.inRound = False

	def update(self):
		pass

class AIPlayer(MPlayer):
	def update(self):
		from Script import MGlobalData
		if self.inRound:
			MGlobalData.Round.playTile(self, self.hand.tiles[-1])
import random

class MWall(object):
	"""
	Wall: 牌山
	"""
	def __init__(self, hasHoleCards:bool, tiles:list) -> None:
		super().__init__()
		self.tiles = tiles
		self.holeCards = []
		self.hasHoleCards = hasHoleCards

	def shuffle(self):
		random.shuffle(self.tiles)
		if self.hasHoleCards:
			self.holeCards = self.tiles[-14:]
			self.tiles = self.tiles[:-14]

	def draw(self, num):
		ret = self.tiles[:num]
		self.tiles = self.tiles[num:]
		return ret
from Script.Core.MTile import MTile

class MHand(object):
	"""
	Hand: 手牌
	"""
	@staticmethod
	def CreateFromTiles(tiles):
		hand = MHand()
		hand.tiles = tiles
		return hand

	def __init__(self):
		self.tiles = []
		self.drawIn = None

	def __str__(self):
		return " ".join([str(t) for t in self.tiles])

	def copy(self):
		hand = MHand()
		hand.tiles = self.Tiles.copy()
		return hand

	@property
	def Tiles(self):
		return self.tiles

	def setupFromBrief(self, brief):
		briefs = brief.split(" ")
		for bf in briefs:
			tile = MTile(bf)
			self.tiles.append(tile)

	def sort(self):
		dots, bamboo, characters, winds, dragons, jokers = [], [], [], [], [], []
		sortMap = {
			MTile.Dots: lambda tile: dots.append(tile),
			MTile.Bamboo: lambda tile: bamboo.append(tile),
			MTile.Characters: lambda tile: characters.append(tile),
			MTile.Winds: lambda tile: winds.append(tile),
			MTile.Dragons: lambda tile: dragons.append(tile),
			MTile.Jokers: lambda tile: jokers.append(tile),
		}
		for tile in self.tiles:
			if tile.tileType in sortMap:
				sortMap[tile.tileType](tile)
		for tg in [dots, bamboo, characters, winds, dragons, jokers]:
			tg.sort(key=lambda k: k.tileNum)
		tiles = dots + bamboo + characters + winds + dragons + jokers
		assert(len(tiles)==len(self.tiles))
		self.tiles = tiles

	def draw(self, tile):
		self.tiles.append(tile)
		self.drawIn = tile

	def play(self, tile):
		self.tiles.remove(tile)
		self.drawIn = None
		self.sort()
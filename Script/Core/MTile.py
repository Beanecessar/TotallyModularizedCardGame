import math

class MTile(object):
	"""
	Tile: 麻将牌
	TileType: 牌的种类
	TileNum: 牌的点数
	"""
	# TileType
	Null = 			0b00000000
	Dots = 			0b00000001 #筒牌
	Bamboo = 		0b00000010 #条牌
	Characters = 	0b00000100 #万牌
	Winds = 		0b00001000 #风牌
	Dragons = 		0b00010000 #箭牌
	Flowers = 		0b00100000 #花牌
	Seasons = 		0b01000000 #季牌
	Jokers = 		0b10000000 #百搭
	AllType = 		0b11111111
	# TileNum
	Null = 			0b000000000
	One = 			0b000000001
	Two = 			0b000000010
	Three = 		0b000000100
	Four = 			0b000001000
	Five = 			0b000010000
	Six = 			0b000100000
	Seven = 		0b001000000
	Eight = 		0b010000000
	Nine = 			0b100000000
	AllNum = 		0b111111111
	# 简记
	# 1-9筒		1-9p
	# 1-9条		1-9s
	# 1-9万		1-9m
	# 东南西北	1-4z
	# 中发白	5-7z
	# 百搭		a

	@staticmethod
	def CreateFromBrief(brief):
		tile = MTile()
		tile.SetupFromBrief(brief)
		return tile

	@staticmethod
	def CreateFromData(tileType, tileNum):
		tile = MTile()
		tile.tileType, tile.tileNum = tileType, tileNum
		return tile

	def __init__(self):
		self.tileType = self.Null
		self.tileNum = self.Null

	def __str__(self):
		# TODO: 更多百搭
		if self.tileType == self.Jokers:
			return "a"
		numpart = int(math.log(self.tileNum, 2))+1
		if self.tileType == self.Dots:
			return str(numpart)+"p"
		if self.tileType == self.Bamboo:
			return str(numpart)+"s"
		if self.tileType == self.Characters:
			return str(numpart)+"m"
		if self.tileType == self.Winds:
			return str(numpart)+"z"
		if self.tileType == self.Dragons:
			return str(numpart+4)+"z"
		else:
			raise ValueError

	def __repr__(self):
		return "MTile<%s>%X"%(self.__str__(), id(self))

	def __eq__(self, other):
		if isinstance(other, MTile):
			return other.tileType & self.tileType and other.tileNum & self.tileNum
		else:
			return False

	def __add__(self, other):
		if isinstance(other, int):
			return MTile(self.tileType, self.tileNum << other)
		else:
			raise ValueError

	# SetupFromBrief
	__NormalBrief = {
		"1p": (Dots, One), "2p": (Dots, Two), "3p": (Dots, Three), "4p": (Dots, Four), "5p": (Dots, Five), "6p": (Dots, Six), "7p": (Dots, Seven), "8p": (Dots, Eight), "9p": (Dots, Nine), 
		"1s": (Bamboo, One), "2s": (Bamboo, Two), "3s": (Bamboo, Three), "4s": (Bamboo, Four), "5s": (Bamboo, Five), "6s": (Bamboo, Six), "7s": (Bamboo, Seven), "8s": (Bamboo, Eight), "9s": (Bamboo, Nine), 
		"1m": (Characters, One), "2m": (Characters, Two), "3m": (Characters, Three), "4m": (Characters, Four), "5m": (Characters, Five), "6m": (Characters, Six), "7m": (Characters, Seven), "8m": (Characters, Eight), "9m": (Characters, Nine), 
		"1z": (Winds, One), "2z": (Winds, Two), "3z": (Winds, Three), "4z": (Winds, Four), "5z": (Dragons, One), "6z": (Dragons, Two), "7z": (Dragons, Three),
		"a": (AllType, AllNum),
	}
	def SetupFromBrief(self, brief):
		# 解析简记
		assert(brief in self.__NormalBrief)
		self.tileType, self.tileNum = self.__NormalBrief[brief]

AllTiles = [MTile.CreateFromBrief(brief) for brief in MTile._MTile__NormalBrief]
AllNormalTiles = [MTile.CreateFromBrief(brief) for brief in MTile._MTile__NormalBrief if brief != "a"]

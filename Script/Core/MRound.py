import random

from pyxel import play
from Script.Core.MHand import MHand
from Script.Core.MPlayer import Wind, MPlayer, AIPlayer
from Script.Core.MRuler import MRuler
from Script.Core.MWall import MWall

class MRound(object):
	def __init__(self, ruler:MRuler) -> None:
		super().__init__()
		self.ruler = ruler
		self.players = []
		self.banker = None

	def nextPlayer(self, player):
		index = self.players.index(player)
		return self.players[(index+1)%len(self.players)]

	def start(self):
		self.wall = MWall(self.ruler.hasHoleCards, self.ruler.allTiles.copy())
		self.wall.shuffle()
		# for i in range(self.ruler.numOfPlayer):
		# 	hand = MHand()
		# 	self.players.append(MPlayer(hand, self.ruler.startPoints))
		# ----------
		self.players.append(MPlayer(self.ruler.startPoints))
		for i in range(self.ruler.numOfPlayer - 1):
			self.players.append(AIPlayer(self.ruler.startPoints))
		# ----------
		bankerIndex = random.randint(0, len(self.players)-1)
		self.banker = self.players[bankerIndex]
		self.banker.pos = Wind.East
		self.banker.hand.tiles = self.wall.draw(14)
		self.banker.hand.sort()
		self.banker.inRound = True
		for i in range(1, len(self.players)):
			player = self.players[(bankerIndex+i)%len(self.players)]
			player.pos = Wind.East + i
			player.hand.tiles = self.wall.draw(13)
			player.hand.sort()

	def update(self):
		for player in self.players:
			player.update()

	def playTile(self, player, tile):
		player.hand.play(tile)
		player.inRound = False
		nextPlayer = self.nextPlayer(player)
		nextPlayer.inRound = True
		nextPlayer.hand.draw(self.wall.draw(1)[0])
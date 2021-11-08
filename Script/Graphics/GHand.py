import pygame, os
from Script import MGlobalData
from Script.Core.MPlayer import MPlayer
from Script.Graphics.GObject import GObject
from Script.Graphics.GTile import GTile

class GHand(GObject):
	Width = MGlobalData.ScreenWidth
	Height = GTile.Height
	def __init__(self, y, player:MPlayer):
		super().__init__(0, y)
		self.hand = player.hand
		self.player = player

	def update(self):
		pass

	def draw(self, screen):
		if self.hand.drawIn is not None:
			x = (GHand.Width - GTile.Width*len(self.hand.tiles) - 2) / 2
		else:
			x = (GHand.Width - GTile.Width*len(self.hand.tiles)) / 2
		for tile in self.hand.tiles:
			gtile = GTile(x, self.y, tile)
			if tile is self.hand.drawIn:
				gtile.x += 2
			if gtile.isHover():
				gtile.y -= 2
				# if self.player.inRound and pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON):
				# 	MGlobalData.Round.playTile(self.player, tile)
			gtile.draw(screen)
			x += GTile.Width
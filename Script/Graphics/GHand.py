import pygame, os
from Script import MGlobalData
from Script.Core.MPlayer import MPlayer
from Script.Graphics.GObject import GObject
from Script.Graphics.GTile import GTile

class GHand(GObject):
	Width = MGlobalData.ScreenWidth
	Height = GTile.Height
	Spacing = MGlobalData.DrawInSpacing
	def __init__(self, y, player:MPlayer):
		super().__init__(0, y)
		self.hand = player.hand
		self.player = player
		self.gtiles = []

	def update(self):
		pass

	def draw(self, screen):
		self.gtiles.clear()
		if self.hand.drawIn is not None:
			x = (GHand.Width - GTile.Width*len(self.hand.tiles) - 2) / 2
		else:
			x = (GHand.Width - GTile.Width*len(self.hand.tiles)) / 2
		for tile in self.hand.tiles:
			gtile = GTile(x, self.y, tile)
			if tile is self.hand.drawIn:
				gtile.x += GHand.Spacing
			if gtile.isHover():
				gtile.y -= GTile.Height / 10
			gtile.draw(screen)
			x += GTile.Width
			self.gtiles.append(gtile)

	def mouseReleaseEvent(self, event):
		if event.button == 1: # Left Button
			if self.player.inRound:
				for gtile in self.gtiles:
					if gtile.rect.collidepoint(event.pos):
						MGlobalData.Round.playTile(self.player, gtile.tile)
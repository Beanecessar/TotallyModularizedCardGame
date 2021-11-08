import pygame, sys
from Script import MGlobalData
from Script.Core.MRuler import MRuler
from Script.Core.MRound import MRound
from Script.Graphics.GTable import GTable
from Script.Graphics.GHand import GHand
from Script.Graphics.GTile import GTile

class MApplication:
	def __init__(self):
		MGlobalData.App = self
		pygame.init()
		MApplication.Init()
		self.screen = pygame.display.set_mode(MGlobalData.ScreenSize)
		self.table = GTable((MGlobalData.ScreenWidth-GTable.Width)/2, 25)
		self.round = MRound(MRuler())
		self.round.start()
		MGlobalData.Round = self.round
		self.player = self.round.players[0]
		self.hand = GHand(MGlobalData.ScreenHeight - GTile.Height - 5, self.player)

	@staticmethod
	def Init():
		GTile.Init()
		GTable.Init()

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				elif event.type == pygame.MOUSEBUTTONUP:
					self.mouseReleaseEvent(event)
			self.update()
			self.draw(self.screen)
			pygame.display.flip()

	def exit(self):
		pygame.quit()
		sys.exit()

	def update(self):
		self.round.update()
		self.hand.update()

	def draw(self, screen):
		screen.fill((0,0,0))
		self.table.draw(screen)
		self.hand.draw(screen)

	def mouseReleaseEvent(self, event):
		if self.hand.rect.collidepoint(event.pos):
			self.hand.mouseReleaseEvent(event)
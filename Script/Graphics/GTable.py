import pygame
from Script.Graphics.GObject import GObject
from Script.Graphics.GTile import GTile

class GTable(GObject):
	Image = None
	Width = 200 * 3
	Height = 120 * 3
	def __init__(self, x, y) -> None:
		super().__init__(x, y)

	@staticmethod
	def Init():
		import os
		GTable.Image = pygame.image.load(os.path.abspath("Resource\\Table.png"))

	def update(self):
		pass
	
	def draw(self, screen):
		screen.blit(pygame.transform.scale(GTable.Image, (GTable.Width, GTable.Height)), self.rect)
import pygame
from Script.Core.MTile import MTile
from Script.Graphics.GObject import GObject

class GTile(GObject):
	Image = None
	Width = 18 * 3
	Height = 24 * 3
	ImgRect = {
		"1p": (0,	0,	18,	24),
		"2p": (18,	0,	18,	24),
		"3p": (36,	0,	18,	24),
		"4p": (54,	0,	18,	24),
		"5p": (72,	0,	18,	24),
		"6p": (90,	0,	18,	24),
		"7p": (108,	0,	18,	24),
		"8p": (126,	0,	18,	24),
		"9p": (144,	0,	18,	24),
		"1s": (0,	24,	18,	24),
		"2s": (18,	24,	18,	24),
		"3s": (36,	24,	18,	24),
		"4s": (54,	24,	18,	24),
		"5s": (72,	24,	18,	24),
		"6s": (90,	24,	18,	24),
		"7s": (108,	24,	18,	24),
		"8s": (126,	24,	18,	24),
		"9s": (144,	24,	18,	24),
		"1m": (0,	48,	18,	24),
		"2m": (18,	48,	18,	24),
		"3m": (36,	48,	18,	24),
		"4m": (54,	48,	18,	24),
		"5m": (72,	48,	18,	24),
		"6m": (90,	48,	18,	24),
		"7m": (108,	48,	18,	24),
		"8m": (126,	48,	18,	24),
		"9m": (144,	48,	18,	24),
		"1z": (0,	72,	18,	24),
		"2z": (18,	72,	18,	24),
		"3z": (36,	72,	18,	24),
		"4z": (54,	72,	18,	24),
		"5z": (72,	72,	18,	24),
		"6z": (90,	72,	18,	24),
		"7z": (108,	72,	18,	24),
		"0p": (126,	72,	18,	24),
		"0s": (144,	72,	18,	24),
		"0m": (0,	96,	18,	24),
	}
	def __init__(self, x, y, tile:MTile):
		super().__init__(x, y)
		self.imgRect = GTile.ImgRect[str(tile)]
		self.tile = tile

	@staticmethod
	def Init():
		import os
		GTile.Image = pygame.image.load(os.path.abspath("Resource\\Tiles.png"))

	def update(self):
		pass
	
	def draw(self, screen):
		screen.blit(pygame.transform.scale(GTile.Image.subsurface(self.imgRect), (GTile.Width, GTile.Height)), self.rect)

	def isHover(self):
		return self.rect.collidepoint(pygame.mouse.get_pos())
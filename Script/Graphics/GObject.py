import pygame

class GObject(object):
	def __init__(self, x, y) -> None:
		super().__init__()
		self.rect = pygame.Rect(x, y, self.__class__.Width, self.__class__.Height)

	@property
	def x(self):
		return self.rect.x

	@x.setter
	def x(self, value):
		self.rect.x = value

	@property
	def y(self):
		return self.rect.y

	@y.setter
	def y(self, value):
		self.rect.y = value

	def update(self):
		pass

	def draw(self):
		pass
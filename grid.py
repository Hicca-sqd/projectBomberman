import pygame
import settings
class Grid:
	def __init__(self):
		self.grid_lines = [((settings.ICON*i, 0), (settings.ICON*i, settings.HEIGHT)) for i in range(1, settings.W)] + [((0, settings.ICON*i), (settings.WIDTH, settings.ICON*i)) for i in range(1, settings.H)]
	def draw(self, surface):
		for line in self.grid_lines:
			pygame.draw.line(surface, (200, 200, 200), line[0], line[1], 2)

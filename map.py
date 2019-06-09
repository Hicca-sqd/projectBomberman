import settings, time
class Map:
	def __init__(self):
		pass
	def collission(self, X, Y, box, bombs, hero, enemy):
		x = X
		y = Y
		for i in bombs:
			if i.X == X and i.Y == Y:
				x, y = None, i
				break
		cx = X // settings.ICON
		cy = Y // settings.ICON
		if ((cx , cy) in box.immortalBox):
			x, y = None, 3
		if ((cx , cy) in box.chestBox):
			x, y = None, 4
		if (hero.X == X and hero.Y == Y):
			x, y = None, 1
		if (enemy.X == X and enemy.Y == Y):
			x, y = None, 2
		return x, y
	def draw(self, surface, box, bombs, hero, enemy, explossion):
		for i in bombs:
			surface.blit(i.img, (i.X, i.Y))
		for i in explossion:
			surface.blit(i.img, (i.X, i.Y))
		for i in box.immortalBox:
			surface.blit(settings.metalImg, (i[0] * settings.ICON, i[1] * settings.ICON))
		for i in box.loot:
			if (i[2] == 0):
				surface.blit(settings.loot1Img, (i[0] * settings.ICON, i[1] * settings.ICON))
			else:
				surface.blit(settings.loot2Img, (i[0] * settings.ICON, i[1] * settings.ICON))
		for i in box.chestBox:
			surface.blit(settings.boxImg, (i[0] * settings.ICON, i[1] * settings.ICON))
		surface.blit(hero.img, (hero.X, hero.Y))
		surface.blit(enemy.img, (enemy.X, enemy.Y))
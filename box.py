import settings
import random
class Box:
	def __init__(self):
		self.numberOfBox = random.randint(int(settings.W * settings.H * 0.45) - 5, int(settings.W * settings.H * 0.45) + 5)
		self.immortalBox = []
		self.chestBox = []
		self.loot = []
	def reset(self, hero, enemy):
		self.immportalBox = []
		for i in range(int(self.numberOfBox * 0.2)):
			x = random.randint(0, settings.W - 2)
			y = random.randint(0, settings.H - 2)
			while (hero == (x, y) or (abs(hero[0] - x) + abs(hero[1] - y) <= 1) or (abs(enemy[0] - x) + abs(enemy[1] - y) <= 1) or (x, y) in self.immortalBox or (x, y) in self.chestBox):
				x = random.randint(0, settings.W - 2)
				y = random.randint(0, settings.H - 2)
			self.immortalBox.append((x, y))

		for i in range(self.numberOfBox - len(self.immortalBox)):
			x = random.randint(0, settings.W - 2)
			y = random.randint(0, settings.H - 2)
			while (hero == (x, y) or abs(hero[0] - x) + abs(hero[1] - y) <= 1 or (abs(enemy[0] - x) + abs(enemy[1] - y) <= 1) or (x, y) in self.immortalBox or (x, y) in self.chestBox):
				x = random.randint(0, settings.W - 2)
				y = random.randint(0, settings.H - 2)
			self.chestBox.append((x, y))
		for i in range(int(len(self.chestBox) * 0.8)):
			x = self.chestBox[i][0]
			y = self.chestBox[i][1]
			self.loot.append((x, y, random.randint(0, 1)))
		
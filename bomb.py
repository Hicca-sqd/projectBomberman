import settings
import time, sys
import threading
from explosion import Explosion
class Bomb:
	def __init__(self, type, x, y, map, box, bombs, hero, enemy, explosion, r = settings.bombRadius, start = 0):
		self.type = type
		self.r = r
		self.X = x
		self.Y = y
		self.img = settings.bombImg
		if start == 0:
			self.start = time.time()
		else:
			self.start = time.time() - start
		self.k = 2.0
		self.explode = False
		self.changeImg = 1
		self.addK = 1
		self.thread = threading.Timer(0.0, self.check, [map, box, bombs, hero, enemy, explosion])
		self.thread.start()
	def check(self, map, box, bombs, hero, enemy, explosion):
		if self.explode == False and time.time() - self.start >= 7.0:
			self.explosion(map, box, bombs, hero, enemy, explosion)
		if time.time() - self.start < 7.0:
			if time.time() - self.start > self.k:
				self.changeImg = 1 - self.changeImg
				self.addK += 1
				self.k += 2 / self.addK
			if self.changeImg:
				self.img = settings.bombImg
			else: 
				self.img = settings.bomb2Img
		self.thread = threading.Timer(0.0, self.check, [map, box, bombs, hero, enemy, explosion])
		self.thread.start()
	def explosion(self, map, box, bombs, hero, enemy, explosion):
		self.explode = True
		if self.type == 1:
			hero.bombs -= 1
		else:
			enemy.bombs -= 1
		bombs.remove(self)
		explosion.append(Explosion(self.X, self.Y))
		for i in range(self.X, min(self.X + self.r + 1, settings.WIDTH - settings.ICON + 1), settings.ICON):
			x, y = map.collission(i, self.Y, box, bombs, hero, enemy)
			if x != None or (type(y) == int and (y == 1 or y == 2)):
				explosion.append(Explosion(i, self.Y))
			if x == None and type(y) == int and y == 3:
				break
			if x == None and type(y) == int and y == 4:
				if self.type == 1:
					hero.score += 1
				else:
					enemy.score += 1
				box.chestBox.remove((i // settings.ICON, self.Y // settings.ICON))
				explosion.append(Explosion(i, self.Y))
				break
			if x == None and type(y) != int:
				bombs[bombs.index(y)].start = 7.0
				break
			if x == None and type(y) == int and y == 1:
				hero.alive = False
			if x == None and type(y) == int and y == 2:
				enemy.alive = False
				
		for i in range(self.X - settings.ICON, max(-1, self.X - self.r - 1), -settings.ICON):
			x, y = map.collission(i, self.Y, box, bombs, hero, enemy)
			if x != None or (type(y) == int and y == 1):
				explosion.append(Explosion(i, self.Y))
			if x == None and type(y) == int and y == 3:
				break
			if x == None and type(y) == int and y == 4:
				if self.type == 1:
					hero.score += 1
				else:
					enemy.score += 1
				box.chestBox.remove((i // settings.ICON, self.Y // settings.ICON))
				explosion.append(Explosion(i, self.Y))
				break
			if x == None and type(y) != int:
				bombs[bombs.index(y)].start = 7.0
				break
			if x == None and type(y) == int and y == 1:
				hero.alive = False
			if x == None and type(y) == int and y == 2:
				enemy.alive = False
		for i in range(settings.ICON + self.Y, min(self.Y + self.r + 1, settings.HEIGHT - settings.ICON + 1), settings.ICON):
			x, y = map.collission(self.X, i, box, bombs, hero, enemy)
			if x != None or (type(y) == int and y == 1):
				explosion.append(Explosion(self.X, i))
			if x == None and type(y) == int and y == 3:
				break
			if x == None and type(y) == int and y == 4:
				if self.type == 1:
					hero.score += 1
				else:
					enemy.score += 1
				box.chestBox.remove((self.X // settings.ICON, i // settings.ICON))
				explosion.append(Explosion(self.X, i))
				break
			if x == None and type(y) != int:
				bombs[bombs.index(y)].start = 7.0
				break
			if x == None and type(y) == int and y == 1:
				hero.alive = False
			if x == None and type(y) == int and y == 2:
				enemy.alive = False
		for i in range(self.Y - settings.ICON, max(-1, self.Y - self.r - 1), -settings.ICON):
			x, y = map.collission(self.X, i, box, bombs, hero, enemy)
			if x != None or (type(y) == int and y == 1):
				explosion.append(Explosion(self.X, i))
			if x == None and type(y) == int and y == 3:
				break
			if x == None and type(y) == int and y == 4:
				if self.type == 1:
					hero.score += 1
				else:
					enemy.score += 1
				box.chestBox.remove((self.X // settings.ICON, i // settings.ICON))
				explosion.append(Explosion(self.X, i))
				break
			if x == None and type(y) != int:
				bombs[bombs.index(y)].start = 7.0
				break
			if x == None and type(y) == int and y == 1:
				hero.alive = False
			if x == None and type(y) == int and y == 2:
				enemy.alive = False
		self.thread._Thread__stop()


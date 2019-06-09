import pygame
from pygame.locals import *
import settings, sys
from hero import Hero
from bomb import Bomb
from grid import Grid
from map import Map
from box import Box
import time, threading


def check(x):
	return max(0, min(settings.WIDTH - settings.ICON, x))
def tableDraw():
			
	textsurface = myfont.render("Hero: {}, alive:{}".format(hero.score, hero.alive), False, (255, 255, 255))
	surface.blit(textsurface,(620, 50))
	textsurface = myfont.render("Enemy: {}, alive:{}".format(enemy.score, enemy.alive), False, (255, 255, 255))
	surface.blit(textsurface,(620, 80))
	textsurface = myfont.render(str(step // 100) + "/100", False, (255, 255, 255))
	surface.blit(textsurface,(620, 120))
	
	pygame.display.update()
def Draw():
	surface.fill((0,0,0))
	grid.draw(surface)
	map.draw(surface, box, bombs, hero, enemy, explosion)
	tableDraw()
	pygame.display.update()
def KillThreads():
	for thread in threading.enumerate():
		if thread.isAlive():
		    try:
		        thread._Thread__stop()
		    except:
	        	print(str(thread.getName()) + ' could not be terminated')
def Winner():
	if hero.alive:
		return "Hero is a Winner"
	if enemy.alive:
		return "Enemy is a Winner"
	if hero.score > enemy.score:
		return "Hero is a Winner"
	if hero.score < enemy.score:
		return "Enemy is a Winner"
	return "Draw"
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 18)
gameOver = pygame.font.SysFont('Comic Sans MS', 30)

clock = pygame.time.Clock()
surface = pygame.display.set_mode((settings.WIDTH + 200, settings.HEIGHT))

grid = Grid()
hero = Hero(1)
enemy = Hero(2, settings.WIDTH - settings.ICON, settings.WIDTH - settings.ICON)
map = Map()
box = Box()
box.reset((hero.X // settings.ICON, hero.Y // settings.ICON), (enemy.X // settings.ICON, enemy.Y // settings.ICON))
bombs = []
explosion = []
running = True


lastKey = None
step = 0
gameState = True

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
			sys.exit()
		elif gameState and event.type == KEYDOWN:
			if event.key == K_p:
				if (enemy.bomb_n > enemy.bombs):
					free = True
					for i in bombs:
						if (i.X == enemy.X and i.Y == enemy.Y):
							free = False
							break
					if free:
						bombs.append(Bomb(enemy.type, enemy.X, enemy.Y, map, box, bombs, hero, enemy, explosion, enemy.bomb_r))
						enemy.bombs += 1
			if event.key == K_SPACE:
				if (hero.bomb_n > hero.bombs):
					free = True
					for i in bombs:
						if (i.X == hero.X and i.Y == hero.Y):
							free = False
							break
					if free:
						bombs.append(Bomb(hero.type, hero.X, hero.Y, map, box, bombs, hero, enemy, explosion, hero.bomb_r))
						hero.bombs += 1
			else:
				key = event.key
				x = None
				y = None
				if (key == K_w):
					x, y = map.collission(hero.X, check(hero.Y - settings.SPEED), box, bombs, hero, enemy) 
				elif (key == K_s):
					x, y = map.collission(hero.X, check(hero.Y + settings.SPEED), box, bombs, hero, enemy)
				elif (key == K_a):
					x, y = map.collission(check(hero.X - settings.SPEED), hero.Y, box, bombs, hero, enemy)
				elif (key == K_d):
					x, y = map.collission(check(hero.X + settings.SPEED), hero.Y, box, bombs, hero, enemy)
				if (x != None):
					hero.X, hero.Y = x, y
				x = None
				y = None
				if (key == K_UP):
					x, y = map.collission(enemy.X, check(enemy.Y - settings.SPEED), box, bombs, hero, enemy) 
				elif (key == K_DOWN):
					x, y = map.collission(enemy.X, check(enemy.Y + settings.SPEED), box, bombs, hero, enemy)
				elif (key == K_LEFT):
					x, y = map.collission(check(enemy.X - settings.SPEED), enemy.Y, box, bombs, hero, enemy)
				elif (key == K_RIGHT):
					x, y = map.collission(check(enemy.X + settings.SPEED), enemy.Y, box, bombs, hero, enemy)
				if (x != None):
					enemy.X, enemy.Y = x, y
	if gameState:
		hero.takeLoot(box)
		enemy.takeLoot(box)
		for i in explosion:
			if i.explode:
				explosion.remove(i)
		Draw()
		# hero.smoothMove(grid, surface, clock, bombs)
	if (gameState == True and (hero.alive == False or enemy.alive == False)):
		KillThreads()
		Draw()
		rect = pygame.Surface((settings.WIDTH, settings.HEIGHT), pygame.SRCALPHA) 
		rect.fill((0,0,0, 128))
		rect.blit(surface, (0,0))
		pygame.display.update()
		text = gameOver.render(Winner(), False, (2, 180, 180))
		surface.blit(text, (250, 250))
		pygame.display.update()
		gameState = False
	if step > 10000:
		hero.alive = False
		enemy.alive = False
	clock.tick(60)
	step += 1


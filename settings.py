import pygame
WIDTH = 600
HEIGHT = 600
W = 13
H = 13
SPEED = 50
ICON = 50
bombRadius = 100 # pixels

heroIcon = './img/hero.png'
heroImg = pygame.image.load(heroIcon)
heroImg = pygame.transform.scale(heroImg, (ICON, ICON))


enemyIcon = './img/enemy.png'
enemyImg = pygame.image.load(enemyIcon)
enemyImg = pygame.transform.scale(enemyImg, (ICON, ICON))

metalIcon = './img/metal.jpg'
metalImg = pygame.image.load(metalIcon)
metalImg = pygame.transform.scale(metalImg, (ICON, ICON))

boxIcon = './img/box.png'
boxImg = pygame.image.load(boxIcon)
boxImg = pygame.transform.scale(boxImg, (ICON, ICON))

bombIcon = './img/bomb.png'
bombImg = pygame.image.load(bombIcon)
bombImg = pygame.transform.scale(bombImg, (ICON, ICON))

bomb2Icon = './img/bomb2.png'
bomb2Img = pygame.image.load(bomb2Icon)
bomb2Img = pygame.transform.scale(bomb2Img, (ICON, ICON))

bomb3Icon = './img/explosion.gif'
bomb3Img = pygame.image.load(bomb3Icon)
bomb3Img = pygame.transform.scale(bomb3Img, (ICON, ICON))

loot1Icon = './img/loot1.png'
loot1Img = pygame.image.load(loot1Icon)
loot1Img = pygame.transform.scale(loot1Img, (ICON, ICON))

loot2Icon = './img/loot2.png'
loot2Img = pygame.image.load(loot2Icon)
loot2Img = pygame.transform.scale(loot2Img, (ICON, ICON))

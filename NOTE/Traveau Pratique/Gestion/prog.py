#Coding:utf-8
import pygame
from pygame.locals import*

pygame.init()
fenetre = pygame.display.set_mode((876,1200), RESIZABLE)
fond1 = pygame.image.load("a1.jpg").convert_alpha()
fond2 = pygame.image.load("a2.png")
pax = 0
pay = 0
position_fond1 = fond1.get_rect()
fenetre.blit(fond1, position_fond1)
fenetre.blit(fond2,(pax,pay))

pygame.display.flip()

pygame.key.set_repeat(400, 3)
continuer = 1
while continuer:
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				if event.type == MOUSEMOTION:
					pax = event.pos[0]
					pay = event.pos[1]
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_DOWN or event.key == K_8:
				position_fond1 = position_fond1.move(0,10)

			if event.key == K_UP or event.key == K_2:
				position_fond1 = position_fond1.move(0,-10)

			if event.key == K_RIGHT or event.key == K_4:
				position_fond1 = position_fond1.move(10,0)

			if event.key == K_LEFT or event.key == K_6:
				position_fond1 = position_fond1.move(-10,0)
	fenetre.blit(fond1, position_fond1)
	fenetre.blit(fond2, (pax,pay))
	pygame.display.flip()
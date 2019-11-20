import pygame
import sprite

#desenhando fundo do menu
def menu(screen):
	global play_press, credits_press

	screen.blit(sprite.menu, (0,0))

	play_press = screen.blit(sprite.button_play, (400, 225))
	credits_press = screen.blit(sprite.button_credits, (750, 400))
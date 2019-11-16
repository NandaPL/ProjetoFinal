import pygame
import sprites
pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Projeto Final')
pygame.display.flip()
SPRITES = "sprites/"

background = pygame.image.load(
SPRITES+"background-menu.png").convert_alpha()

def redraw_menu():
    screen.blit(background, (0, 0))
    


run = init = True


while run:
    if init:
        redraw_menu()
        
        pygame.display.update()

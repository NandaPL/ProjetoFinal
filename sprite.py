import pygame
from main import height,width

pygame.init()
pygame.display.set_mode((width, height))

# função pra facilitar o carregamento da imagem
def load_imagem(image):
    return pygame.image.load(image).convert_alpha()

button_play = load_imagem("sprites/play.jpg")

button_credits = load_imagem("sprites/credit.jpg")

game = load_imagem("sprites/battle.jpg")

menu = load_imagem("sprites/background.jpg")

knight = load_imagem("sprites/Knight/knight.png")
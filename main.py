from full_gameplay import game
from show_credits import run_credits
from all_sprites import *
import sprites
import pygame
import sounds

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

width = 800
height = 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Forest Viking')


# função pra facilitar o carregamento da imagem
def load_image(image):
    return pygame.image.load(image).convert_alpha()


def redraw_knight(x, y):
    screen.blit(knight, (x, y))


global knight
knight = load_image(sprite_idle[1])
frame = 8

pygame.mouse. set_visible(False)
cursor = load_image(s_cursor)
button_play = load_image(s_play)
button_credits = load_image(s_credits)
back_menu = load_image(s_background_menu)
name_game = load_image(n_game)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()


def menu():
    global play_press, credits_press
    screen.blit(back_menu, (0, 0))
    play_press = screen.blit(button_play, (300, 200))
    credits_press = screen.blit(button_credits, (285, 350))
    screen.blit(name_game, (200, 50))


run = True
initial = True
button_pressed = False
# background sound

pygame.mixer.music.load("sounds/Dream_Island.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

while run:

    if initial:
        menu()

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            button_pressed = True

        if event.type == pygame.QUIT:
            run = False

    if button_pressed:  # aqui eu verifico se o play foi
        mouse = pygame.mouse.get_pos()
        if mouse[0] > 314 and mouse[0] < 481:
            if mouse[1] > 214 and mouse[1] < 274:
                game()
        if mouse[0] > 294 and mouse[0] < 502:
            if mouse[1] > 361 and mouse[1] < 407:
                run_credits()
        button_pressed = False

    if frame == 96:
        frame = 8
    if frame >= 8:
        if frame % 8 == 0:
            knight = load_image(sprite_idle[int(frame/8)])
    frame += 1

    redraw_knight(50, 300)
    redraw_knight(650, 300)

    if pygame.mouse. get_focused():
        mouse = pygame.mouse.get_pos()
        screen.blit(cursor, mouse)
    # background sound
    # pygame.mixer.music.load("sounds/Dream_Island.mp3")
    # pygame.mixer.music.set_volume(1)
    # pygame.mixer.music.play(-1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

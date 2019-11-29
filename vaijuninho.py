import pygame
import sprites
from all_sprites import *
pygame.init()


def game():

    # função pra facilitar o carregamento da imagem
    def load_imagem(caminho):
        return pygame.image.load(caminho).convert_alpha()

    def redraw_background():
        screen.blit(background, (0, 0))

    def redraw_knight(x, y):
        screen.blit(knight, (x, y))

    def change_sprite(ação, pos):
        knight = load_imagem(ação[pos])
        return knight
    # ação: se refere ao tipo de ação no "all_spritess"
    # pos: referente ao numero do sprite no dicionario

    largura = 800
    altura = 450
    screen = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Projeto Final')

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    global knight
    knight = load_imagem(s_inicial)
    background = load_imagem(s_background_game)
    button_back = load_imagem(s_back)
    pygame.mouse. set_visible(False)
    cursor = load_imagem(s_cursor)

    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('couriernew', 55)
    clock = pygame.time.Clock()
    counter, text = 180000, '03:00'.rjust(3)

    x, y = 0, 220  # posição inicial do personagem
    x_speed = y_speed = 2
    move_sprite = ViraVira = False
    lado = "right"
    frame = 0
    f_attack = 0

    pressed_up = pressed_down = pressed_left = pressed_right = pressed_attack = False
    mouse_pressed = False

    run = init = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                counter -= 1000
                if counter >= 0:
                    minutos = int(counter/60000)
                    segundos = int((counter/1000)-minutos*60)

                    minutos = str(minutos)
                    segundos = str(segundos)

                    if len(segundos) == 1:
                        segundos = '0'+segundos
                    text = '0'+minutos+":"+segundos
                else:
                    text = 'boom!'
                    counter = 180000

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True

            # aqui ele verifica se alguma tecla foi pressionado e muda a coordenada
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pressed_up = True
                if event.key == pygame.K_DOWN:
                    pressed_down = True
                if event.key == pygame.K_LEFT:
                    pressed_left = True
                if event.key == pygame.K_RIGHT:
                    pressed_right = True
                if event.key == pygame.K_z:
                    pressed_attack = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    pressed_up = False
                if event.key == pygame.K_DOWN:
                    pressed_down = False
                if event.key == pygame.K_LEFT:
                    pressed_left = False
                if event.key == pygame.K_RIGHT:
                    pressed_right = False

            # aqui ele sai do loop quando aperta no "X"
            if event.type == pygame.QUIT:
                run = False

        if mouse_pressed is True:
            mouse = pygame.mouse. get_pos()
            if mouse[0] > 20 and mouse[0] < 100:
                if mouse[1] > 21 and mouse[1] < 48:
                    run = False
            mouse_pressed = False

        if pressed_attack is False:
            if pressed_up:
                y -= y_speed
                move_sprite = True

            if pressed_down:
                y += y_speed
                move_sprite = True

            if pressed_left:
                x -= x_speed
                if lado == "right":
                    ViraVira = True
                    lado = "left"
                move_sprite = True

            elif pressed_right:
                x += x_speed
                if lado == "left":
                    ViraVira = True
                    lado = "right"
                move_sprite = True

        if move_sprite is True:  # verifica se teve movimento
            if frame == 48:
                frame = 0
            else:
                if frame % 8 == 0 or frame == 0:
                    knight = change_sprite(sprite_walk, frame)
                    if lado == "left":
                        knight = pygame.transform.flip(knight, True, False)
                frame += 1
        move_sprite = False

        if ViraVira is True:
            knight = pygame.transform.flip(knight, True, False)
            if lado == "right":
                x += 25
            if lado == "left":
                x -= 25
            ViraVira = False

        if pressed_attack is True:
            if f_attack == 32:
                f_attack = 0
                pressed_attack = False
                knight = load_imagem(s_inicial)
                if lado == "left":
                    knight = pygame.transform.flip(knight, True, False)
            else:
                if f_attack % 8 == 0 or f_attack == 0:
                    knight = change_sprite(sprite_attack, f_attack)
                    if lado == "left":
                        knight = pygame.transform.flip(knight, True, False)
                f_attack += 1

        redraw_background()  # redesenhando a tela de fundo
        redraw_knight(x, y)  # redesenhando o personagem na posição (x, y)

        screen.blit(font.render(text, True, WHITE), [600, 0])  # desenhando o cronometro na tela na posição (600, 0)
        screen.blit(button_back, [0, 0])

        if pygame.mouse. get_focused():
            mouse = pygame.mouse.get_pos()
            screen.blit(cursor, mouse)

        pygame.display.flip()  # Atualizando a tela
        clock.tick(60)  # aqui eu garanto que o programa fique rodando a 60 fps

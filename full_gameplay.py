import pygame
import sprites
from all_sprites import *
from random import randint
pygame.init()


def game():

    global lifes

    lifes = 3

    # função pra facilitar o carregamento da imagem
    def load_image(way):
        return pygame.image.load(way).convert_alpha()

    def redraw_background():
        screen.blit(background, (0, 0))

    def redraw_knight(x, y):
        screen.blit(knight, (x, y))

    def change_sprite(action, pos):
        knight = load_image(action[pos])
        return knight
    # ação: se refere ao tipo de ação no "all_spritess"
    # pos: referente ao numero do sprite no dicionario

    width = 800
    height = 450
    screen = pygame.display.set_mode((width, height))

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    global knight
    knight = load_image(s_inicial)

    global inimigo
    inimigo = load_image(sprite_golem_walk[1])

    list_inimigo = [inimigo]
    ind_inimigo = [8]
    pos_inimigo = [[400, 300]]
    pos_spawn = [[-20, 300], [-20, 500], [900, 300], [900, 500]]
    time_spawn = 0

    background = load_image(s_background_game)
    button_back = load_image(s_back)
    pygame.mouse. set_visible(False)
    cursor = load_image(s_cursor)
    life = load_image(s_life)

    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('couriernew', 55)
    clock = pygame.time.Clock()
    counter, text = 120000, '02:00'.rjust(3)

    x, y = 0, 220  # posição inicial do personagem
    x_speed = y_speed = 2
    move_sprite = turn = False
    side = "right"
    frame = 8
    f_attack = 0

    pressed_up = pressed_down = pressed_left = pressed_right = pressed_attack = False
    mouse_pressed = False

    run = init = True


    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:

                while len(list_inimigo) < 4:
                    time_spawn += 1
                    if time_spawn > 3:
                        inimigo2 = load_image(sprite_golem_walk[1])
                        list_inimigo.append(inimigo2)
                        ind_inimigo.append(8)
                        pos_inimigo.append(pos_spawn[randint(0, 3)])
                        time_spawn = 0

                counter -= 1000
                if counter >= 0:
                    minutes = int(counter/60000)
                    seconds = int((counter/1000)-minutes*60)

                    minutes = str(minutes)
                    seconds = str(seconds)

                    if len(seconds) == 1:
                        seconds = '0'+seconds
                    text = '0'+minutes+":"+seconds
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
            if mouse[0] > 14 and mouse[0] < 95:
                if mouse[1] > 395 and mouse[1] < 426:
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
                if side == "right":
                    turn = True
                    side = "left"
                move_sprite = True

            elif pressed_right:
                x += x_speed
                if side == "left":
                    turn = True
                    side = "right"
                move_sprite = True

        if turn is True:
            knight = pygame.transform.flip(knight, True, False)
            if side == "right":
                x += 49
            if side == "left":
                x -= 49
            turn = False

        if move_sprite is True:  # verifica se teve movimento
            if frame == 48:
                frame = 8
            else:
                if frame % 8 == 0:
                    knight = change_sprite(sprite_walk, int (frame/8))
                    if side == "left":
                        knight = pygame.transform.flip(knight, True, False)
                frame += 1
        move_sprite = False

        if pressed_attack is True:
            if f_attack == 32:
                f_attack = 0
                pressed_attack = False
                knight = load_image(s_inicial)
                if side == "left":
                    knight = pygame.transform.flip(knight, True, False)
            else:
                if f_attack % 8 == 0 or f_attack == 0:
                    knight = change_sprite(sprite_attack, f_attack)
                    if side == "left":
                        knight = pygame.transform.flip(knight, True, False)
                f_attack += 1

        for i in range(len(list_inimigo)):
            if pos_inimigo[i][0] != x or pos_inimigo[i][1] != y:

                velo_golem = 0.3

                if pos_inimigo[i][0] > x:
                    if pos_inimigo[i][1] < y:
                        pos_inimigo[i][0] -= velo_golem
                        pos_inimigo[i][1] += velo_golem

                    if pos_inimigo[i][1] > y:
                        pos_inimigo[i][0] -= velo_golem
                        pos_inimigo[i][1] -= velo_golem

                elif pos_inimigo[i][0] < x:
                    if pos_inimigo[i][1] < y:
                        pos_inimigo[i][0] += velo_golem
                        pos_inimigo[i][1] += velo_golem

                    if pos_inimigo[i][1] > y:
                        pos_inimigo[i][0] += velo_golem
                        pos_inimigo[i][1] -= velo_golem
                
                elif pos_inimigo[i][0] == x:
                    if y - pos_inimigo[i][1] > 0:
                        pos_inimigo[i][1] += velo_golem
                    if y - pos_inimigo[i][1] < 0:
                        pos_inimigo[i][1] -= velo_golem

                elif pos_inimigo[i][1] == y:
                    if x - pos_inimigo[i][0] > 0:
                        pos_inimigo[i][0] += velo_golem
                    if x - pos_inimigo[i][0] < 0:
                        pos_inimigo[i][0] -= velo_golem

        for i in range(len(list_inimigo)):
            if ind_inimigo[i] == 48:
                ind_inimigo[i] = 8
            if ind_inimigo[i] >= 8:
                if ind_inimigo[i] % 8 == 0:
                    list_inimigo[i] = load_image(sprite_golem_walk[int (ind_inimigo[i]/8)])
                ind_inimigo[i] += 1

        redraw_background()  # redesenhando a tela de fundo
        redraw_knight(x, y)  # redesenhando o personagem na posição (x, y)
        for i in range(len(pos_inimigo)):
            screen.blit(list_inimigo[i], pos_inimigo[i])
        screen.blit(font.render(text, True, WHITE), [600, 0])  # desenhando o cronometro na tela na posição (600, 0)

        l1 = life
        l2 = life
        l3 = life

        list_life = [l1, l2, l3]

        pos = 1
        a = 0 
        screen.blit(list_life[0], [0, 0])

        for pos in range(len(list_life) - 1):
            a = a + 35
            screen.blit(list_life[pos], [a, 0])
        
        screen.blit(button_back, [0, 381])

        if pygame.mouse. get_focused():
            mouse = pygame.mouse.get_pos()
            screen.blit(cursor, mouse)

        pygame.display.flip()  # Atualizando a tela
        clock.tick(60)  # aqui eu garanto que o programa fique rodando a 60 fps

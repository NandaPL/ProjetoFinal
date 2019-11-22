import pygame
import sprites
from all_sprites import *
pygame.init()


def redraw_background():
    screen.blit(background, (0, 0))


def redraw_knight(x, y):
    screen.blit(knight, (x, y))


# função pra facilitar o carregamento da imagem
def load_imagem(caminho):
    return pygame.image.load(caminho).convert_alpha()


def change_sprite(ação, frame):
    knight = load_imagem(ação[frame])
    return knight
# ação: se refere ao tipo de ação da lista de movimentos
# frame: referente ao numero do sprite no dicionario

largura = 800
altura = 450
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Projeto Final')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

global knight
knight = load_imagem(s_inicial)
background = load_imagem(s_background)

# aqui eu estou setando um tempo de 1000 milisegundos para esse evento
# ser chamado a cada segundo
pygame.time.set_timer(pygame.USEREVENT, 1000)

# aqui eu defino uma fonte
font = pygame.font.SysFont(None, 55)

clock = pygame.time.Clock()
counter, text = 180000, ' 03:00'.rjust(3) # 3 minutos equivale a 180.000 milisegundos
# Não lembro pq coloquei em milisegundos mas ta funcionando !!!! hehe

x, y = 0, 300 # posição inicial do personagem
x_speed = y_speed = 2
move_sprite = ViraVira = False
lado = "right"
frame = 0

pressed_up = pressed_down = pressed_left = pressed_right = False

run = init = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: # esse evento acontece ao decorrer de 1 segundo
            counter -= 1000 # retiro 1 segundo
            if counter >= 0:
                # convertendo para o formato mm:ss
                minutos = int(counter/60000)
                segundos = int((counter/1000)-minutos*60)

                minutos = str(minutos)
                segundos = str(segundos)

                if len(segundos) == 1: # aqui se for um numero de 0 a 9 ele coloca um zero na frente pra ficar bunitin
                    segundos = '0'+segundos
                text = '0'+minutos+":"+segundos
            else:
                # aqui se o tempo acabar e ainda tiver vidas ele ganha sei la
                text = 'boom!'
                counter = 180000 # botei isso aqui so pra ficar em um loop bunitin mas não vai ficar assim

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

    if pressed_right:
        x += x_speed
        if lado == "left":
            ViraVira = True
            lado = "right"
        move_sprite = True
    
    if move_sprite == True:  # verifica se teve movimento 
        if frame == 48:
            frame = 0
        else:
            if frame % 8 == 0 or frame == 0:
                knight = change_sprite(sprite_walk, frame)
                if lado == "left":
                    knight = pygame.transform.flip(knight, True, False)
            frame += 1
    move_sprite = False

    if ViraVira == True:
        knight = pygame.transform.flip(knight, True, False)
        ViraVira = False

    redraw_background() # redesenhando a tela de fundo
    redraw_knight(x, y) # redesenhando o personagem na posição (x, y)

    screen.blit(font.render(text, True, WHITE), [600, 0]) # desenhando o cronometro na tela na posição (600, 0)

    pygame.display.flip() # Atualizando a tela
    clock.tick(60) # aqui eu garanto que o programa fique rodando a 60 fps (ui que xiqui !!)

pygame.quit()
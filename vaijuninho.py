import pygame
pygame.init()

def redraw_background():
    screen.blit(background, (0, 0))

# função pra facilitar o carregamento da imagem
def load_imagem(caminho):
    return pygame.image.load(caminho).convert_alpha()

def redraw_knight(x, y):
    screen.blit(knight, (x, y))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

largura = 800
altura = 450
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Projeto Final')

global knight
background = load_imagem("sprites/battle.jpg")
knight = load_imagem("sprites/Knight/knight.png")

run = init = True

# aqui eu estou setando um tempo de 1000 milisegundos para esse evento
# ser chamado a cada segundo
pygame.time.set_timer(pygame.USEREVENT, 1000)

# aqui eu defino uma fonte
font = pygame.font.SysFont(None, 55)

clock = pygame.time.Clock()
counter, text = 180000, ' 03:00'.rjust(3) # 3 minutos equivale a 180.000 milisegundos
# Não lembro pq coloquei em milisegundos mas ta funcionando !!!! hehe

x, y = 0, 300 # posição inicial do personagem
x_speed = y_speed = 3
ViraVira = 1
lado = 1

pressed_up = pressed_down = pressed_left = pressed_right = False

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
                if lado == 1:
                    ViraVira = -1
                    lado = -1
            if event.key == pygame.K_RIGHT:
                pressed_right = True
                if lado == -1:
                    ViraVira = -1
                    lado = 1

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
    if pressed_down:
        y += y_speed
    if pressed_left:
        x -= x_speed
    if pressed_right:
        x += x_speed

    if ViraVira == -1:
        knight = pygame.transform.flip(knight, True, False)
    elif ViraVira == 1:
        knight = pygame.transform.flip(knight, False, False)
    
    ViraVira = 1

    redraw_background() # redesenhando a tela de fundo
    redraw_knight(x, y) # redesenhando o personagem na posição (x, y)

    screen.blit(font.render(text, True, WHITE), [600, 0]) # desenhando o cronometro na tela na posição (600, 0)

    pygame.display.flip() # Atualizando a tela
    clock.tick(60) # aqui eu garanto que o programa fique rodando a 60 fps (ui que xiqui !!)

pygame.quit()
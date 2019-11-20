import pygame
import sprites

pygame.init()
width = 800
height = 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Projeto Final')

# função pra facilitar o carregamento da imagem
def load_imagem(image):
    return pygame.image.load(image).convert_alpha()

button_play = load_imagem("sprites/play.jpg")

button_credits = load_imagem("sprites/credit.jpg")

back_menu = load_imagem("sprites/background.jpg")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# aqui eu estou setando um tempo de 1000 milisegundos para esse evento
# ser chamado a cada segundo
pygame.time.set_timer(pygame.USEREVENT, 1000)

# aqui eu defino uma fonte
font = pygame.font.SysFont(None, 55)

#3 minutos equivale a 180.000 milisegundos
clock = pygame.time.Clock()
counter, text = 180000, ' 03:00'.rjust(3)

# posição inicial do personagem
x, y = 0, 220 

def menu(screen):
	global play_press, credits_press

	screen.blit(back_menu, (0,0))
	play_press = screen.blit(button_play, (300, 150))
	credits_press = screen.blit(button_credits, (600, 380))

run = True
initial = True

while run:

    if initial:
        menu(screen)
    
    for event in pygame.event.get():
        '''if event.type == pygame.USEREVENT: # esse evento acontece ao decorrer de 1 segundo
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
                y -= 20
            if event.key == pygame.K_DOWN:
                y += 20
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_RIGHT:
                x += 20'''

        # aqui ele sai do loop quando aperta no "X"
        if event.type == pygame.QUIT:
            run = False

    
    #screen.blit(font.render(text, True, WHITE), [600, 0]) # desenhando o cronometro na tela

    pygame.display.flip() # Atualizando a tela
    clock.tick(60) # aqui eu garanto que o programa fique rodando a 60 fps (ui que xiqui !!)

pygame.quit()
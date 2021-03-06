from all_sprites import *
import pygame
pygame.init()

def run_credits():

    # função pra facilitar o carregamento da imagem
    def load_image(image):
        return pygame.image.load(image).convert_alpha()

    def redraw_background():
        screen.blit(background, (0, 0))

    width = 800
    height = 450
    screen = pygame.display.set_mode((width, height))

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    background = load_image(s_background_menu)
    button_back = load_image(s_back)
    pygame.mouse. set_visible(False)
    cursor = load_image(s_cursor)

    font = pygame.font.SysFont(None, 23)

    archive = open('credi.txt', 'r')
    text = archive.readlines()
    archive.close()

    run = True
    mouse_pressed = False

    while run:

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True

            if event.type == pygame.QUIT:
                run = False

        if mouse_pressed is True:
            mouse = pygame.mouse. get_pos()
            if mouse[0] > 20 and mouse[0] < 100:
                if mouse[1] > 21 and mouse[1] < 48:
                    run = False
            mouse_pressed = False
        
        screen.fill(BLACK) # deixa o fundo preto

        if height < -480:
            height = 450

        if (height > -480):
            for i in range(len(text)):
                screen.blit(font.render(text[i], True, WHITE), [150, (height + 20 + (i*40))])
            height -= 0.05

        screen.blit(button_back, [0, 0])

        if pygame.mouse. get_focused():
            mouse = pygame.mouse.get_pos()
            screen.blit(cursor, mouse)

        pygame.display.flip()

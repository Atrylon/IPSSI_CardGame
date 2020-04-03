import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()


pygame.display.set_caption('IPSSI Card Game')
screen = pygame.display.set_mode((1280, 910))
font_title = pygame.font.SysFont('Helvetic', 75)
font_text = pygame.font.SysFont('Arial', 25)

click = False



def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():

    global click
    while True:
        screen.fill((192, 192, 192))
        draw_text('IPSSI Card Game', font_title, (0, 0, 0), screen, 50, 20)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(50, 200, 300, 100)
        button_2 = pygame.Rect(50, 350, 300, 100)
        button_3 = pygame.Rect(50, 500, 300, 100)
        button_4 = pygame.Rect(50, 650, 300, 100)

        if button_1.collidepoint(mx, my):
            if click:
                game()
        if button_2.collidepoint(mx, my):
            if click:
                rules()
        if button_3.collidepoint(mx, my):
            if click:
                options()
        if button_4.collidepoint(mx, my):
            if click:
                exit()

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        pygame.draw.rect(screen, (255, 0, 0), button_4)

        screen.blit(font_title.render('Jouer', True, (0, 0, 0)), (88, 225))
        screen.blit(font_title.render('Règles', True, (0, 0, 0)), (88, 375))
        screen.blit(font_title.render('Options', True, (0, 0, 0)), (88, 525))
        screen.blit(font_title.render('Quitter', True, (0, 0, 0)), (88, 675))
        pygame.display.update()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def game():
    running = True
    while running:
        fond = pygame.image.load("ressources/images/background_gwent.jpg").convert()
        screen.blit(fond, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()

def rules():
    running = True
    while running:
        screen.fill((192, 192, 192))

        draw_text('Règles', font_title, (0, 0, 0), screen, 20, 20)

        rules = """Le but du jeu est de se défaire de son adversaire et ainsi d'être le dernier des deux joueurs en vie.

Vous jouez avec un deck de 32 cartes et une main composée de 7 cartes au maximum.

Vous disposez également de 3 ressources nécessaires à l'utilisation de vos cartes : 
    - des points d'action (PA)
    - de l'or (PO)
    - des points de mana (PM)
    
Ces ressources sont générées à chaque tour automatiquement ou à l'aide de cartes, et peuvent être stockées d'un tour
à l'autre.

Au début de votre tour, vous générez des ressources supplémentaires.
Vous piochez automatiquement une carte si votre en main en contient moins de 7.
Vous pouvez ensuite 2 possibilités :
    - Jouer une carte en dépensant le coût nécessaire en ressources.
    - Vous défausser d'une des cartes de votre main.
    
C'est ensuite la fin de votre tour, et le début de celui de votre adversaire.

La partie se terminent lorsqu'un joueur tombe à 0 points de vie.
"""

        # draw_text(rules, font_text, (0, 0, 0), screen, 20, 100)
        blit_text(screen, rules, (20, 120), font_text)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()


def options():
    running = True
    while running:
        screen.fill((192, 192, 192))

        draw_text('Options', font_title, (0, 0, 0), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()


main_menu()
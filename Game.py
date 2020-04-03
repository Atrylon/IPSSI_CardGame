import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()


pygame.display.set_caption('IPSSI Card Game')
screen = pygame.display.set_mode((900, 500))
font = pygame.font.SysFont('Helvetic', 50)
click = False


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():

    while True:
        screen.fill((192, 192, 192))
        draw_text('IPSSI Card Game', font, (0, 0, 0), screen, 50, 20)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                exit()

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)

        screen.blit(font.render('Jouer', True, (0, 0, 0)), (88, 110))
        screen.blit(font.render('Options', True, (0, 0, 0)), (88, 210))
        screen.blit(font.render('Quitter', True, (0, 0, 0)), (88, 310))
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
        screen = pygame.display.set_mode((1280, 910))
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


def options():
    running = True
    while running:
        screen.fill((192, 192, 192))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()


main_menu()
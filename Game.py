import sys
import pygame
from pygame.locals import *

import mysql_connexion
import Cards_CRUD
import Stats
import text_tools
import play

mysql_connexion.init_db()

pygame.init()
pygame.font.init()

pygame.display.set_caption('IPSSI Card Game')
screen = pygame.display.set_mode((1280, 910))
center_x, center_y = 640, 455
GREEN = (40, 230, 120)
font_title = pygame.font.SysFont('Helvetic', 75)
font_text = pygame.font.SysFont('Comic Sans MS,Arial', 20)
son = pygame.mixer.Sound("ressources/sound/The Witcher 3 - Wild Hunt OST - Cloak and Dagger.wav")

heart = pygame.image.load("ressources/images/heart.png").convert_alpha()
heart_small = pygame.transform.scale(heart, (44, 40))
heart_very_small = pygame.transform.scale(heart, (25, 23))

shield = pygame.image.load("ressources/images/shield.png").convert_alpha()
shield_small = pygame.transform.scale(shield, (40, 40))
shield_very_small = pygame.transform.scale(shield, (23, 23))

pm = pygame.image.load("ressources/images/mana.png").convert_alpha()
pm_small = pygame.transform.scale(pm, (40, 40))
pm_very_small = pygame.transform.scale(pm, (23, 23))

po = pygame.image.load("ressources/images/gold.png").convert_alpha()
po_small = pygame.transform.scale(po, (40, 40))
po_very_small = pygame.transform.scale(po, (23, 23))

pa = pygame.image.load("ressources/images/action.png").convert_alpha()
pa_small = pygame.transform.scale(pa, (40, 40))
pa_very_small = pygame.transform.scale(pa, (23, 23))

deck = pygame.image.load("ressources/images/deck.png").convert_alpha()
deck_small = pygame.transform.scale(deck, (40, 40))
deck_very_small = pygame.transform.scale(deck, (23, 23))


def main_menu():
    son.play(loops=0, maxtime=0, fade_ms=0)
    click = False

    while True:
        screen.fill((192, 192, 192))
        text_tools.draw_text('IPSSI Card Game', font_title, (0, 0, 0), screen, 50, 20)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(50, 200, 300, 100)
        button_2 = pygame.Rect(50, 350, 300, 100)
        button_3 = pygame.Rect(50, 500, 300, 100)
        button_4 = pygame.Rect(50, 650, 300, 100)

        if button_1.collidepoint(mx, my):
            if click:
                play.game()
        if button_2.collidepoint(mx, my):
            if click:
                rules()
        if button_3.collidepoint(mx, my):
            if click:
                options()
        if button_4.collidepoint(mx, my):
            if click:
                exit()

        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        pygame.draw.rect(screen, (0, 0, 0), button_3)
        pygame.draw.rect(screen, (0, 0, 0), button_4)

        screen.blit(font_title.render('Jouer', True, (255, 255, 255)), (88, 225))
        screen.blit(font_title.render('Règles', True, (255, 255, 255)), (88, 375))
        screen.blit(font_title.render('Options', True, (255, 255, 255)), (88, 525))
        screen.blit(font_title.render('Quitter', True, (255, 255, 255)), (88, 675))

        text_tools.blit_text(screen, 'Cliquer sur le menu pour y accèder ou appuyer sur \'Echap\' pour revenir au menu précédent', (950, 455), font_text)

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


def rules():
    continuer = True
    while continuer:
        screen.fill((192, 192, 192))
        mx, my = pygame.mouse.get_pos()

        text_tools.draw_text('Règles', font_title, (0, 0, 0), screen, 20, 20)

        rules = """Le but du jeu est de se défaire de son adversaire et ainsi d'être le dernier des deux joueurs en vie.
Chaque joueur possède un maximum de 100 points de vie (PV)      et 30 points de boucliers. 

Des dégats supplémentaires sont infligés en cas de nombre de points de bouclier réduits.

Vous jouez avec un deck     de 32 cartes et une main composée de 7 cartes au maximum.

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

        screen.blit(heart_very_small, (595, 151))
        screen.blit(shield_very_small, (865, 151))

        screen.blit(deck_very_small, (250, 268))

        screen.blit(pa_very_small, (290, 353))
        screen.blit(po_very_small, (178, 383))
        screen.blit(pm_very_small, (290, 413))
        text_tools.blit_text(screen, rules, (20, 120), font_text)

        button_option_1 = pygame.Rect(20, 850, 100, 40)
        pygame.draw.rect(screen, (0, 0, 0), button_option_1)
        text_tools.draw_text('Retour', font_text, (255, 255, 255), screen, 32, 855)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer = False
            if event.type == MOUSEBUTTONDOWN:
                if button_option_1.collidepoint(mx, my) and event.button == 1:
                    continuer = False

        pygame.display.update()


def options():
    continuer = True
    click = False

    while continuer:
        screen.fill((192, 192, 192))
        mx, my = pygame.mouse.get_pos()

        # screen.blit(prompt, prompt_rect)
        # screen.blit(user_input, user_input_rect)

        text_tools.draw_text('Options', font_title, (0, 0, 0), screen, 20, 20)
        button_option_1 = pygame.Rect(50, 200, 600, 100)
        # button_option_2 = pygame.Rect(50, 350, 600, 100)
        button_option_3 = pygame.Rect(50, 500, 600, 100)

        if button_option_1.collidepoint(mx, my):
            if click:
                Cards_CRUD.cards_list()
        # elif button_option_2.collidepoint(mx, my):
        #     if click:
        #         Stats.stats()
        elif button_option_3.collidepoint(mx, my):
            if click:
                continuer = False

        pygame.draw.rect(screen, (0, 0, 0), button_option_1)
        # pygame.draw.rect(screen, (0, 0, 0), button_option_2)
        pygame.draw.rect(screen, (0, 0, 0), button_option_3)

        screen.blit(font_title.render('Gestion des cartes', True, (255, 255, 255)), (88, 225))
        # screen.blit(font_title.render('Statistiques', True, (255, 255, 255)), (88, 375))
        screen.blit(font_title.render('Retour', True, (255, 255, 255)), (88, 525))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_KP_ENTER):
                    continuer = False
                    break
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            # elif event.key == pygame.K_BACKSPACE:
            #     user_input_value = user_input_value[:-1]
            # else:
            #     user_input_value += event.unicode
            # user_input = font_text.render(user_input_value, True, GREEN)
            # user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)

        pygame.display.update()


def end_game():
    running = True
    while running:
        screen.fill((192, 192, 192))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()


main_menu()

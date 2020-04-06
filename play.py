import sys
import pygame
from pygame.locals import *

import mysql_connexion
import text_tools

from Classes.Deck import Deck
from Classes.Player import Player

mysql_connexion.init_db()


def game():
    screen = pygame.display.set_mode((1280, 910))
    font_title = pygame.font.SysFont('Helvetic', 75)
    font_text = pygame.font.SysFont('Comic Sans MS,Arial', 20)

    screen.fill((192, 192, 192))
    cards = mysql_connexion.readCards()

    deck = Deck('Deck de test')
    joueur1 = Player(1, 'Atrylon')
    joueur2 = Player(2, 'Ordinateur')

    for card in cards:
        deck.add_card_to_deck(card)

    print(joueur1.name)
    rect_joueur_2 = pygame.Rect(10, 0, 1260, 100)
    pygame.draw.rect(screen, (0, 0, 0), rect_joueur_2, 25)
    text_tools.draw_text(joueur2.name, font_title, (0, 0, 0), screen, 35, 25)

    rect_joueur_1 = pygame.Rect(10, 810, 1260, 100)
    pygame.draw.rect(screen, (0, 0, 0), rect_joueur_1, 25)
    text_tools.draw_text(joueur1.name, font_title, (0, 0, 0), screen, 35, 835)

    heart = pygame.image.load("ressources/images/heart.png").convert_alpha()
    heart_small = pygame.transform.scale(heart, (44, 40))

    shield = pygame.image.load("ressources/images/shield.png").convert_alpha()
    shield_small = pygame.transform.scale(shield, (40, 40))

    pm = pygame.image.load("ressources/images/mana.png").convert_alpha()
    pm_small = pygame.transform.scale(pm, (40, 40))

    po = pygame.image.load("ressources/images/gold.png").convert_alpha()
    po_small = pygame.transform.scale(po, (40, 40))

    pa = pygame.image.load("ressources/images/action.png").convert_alpha()
    pa_small = pygame.transform.scale(pa, (40, 40))

    for card in deck.cards:
        print(card)
    # for stat in joueur1:
    #     print(stat)
    # print(joueur2)

    nb_cards = len(cards)

    fond_carte_po = pygame.image.load("ressources/fonds de cartes/fond_carte_13.png").convert_alpha()
    fond_carte_pm = pygame.image.load("ressources/fonds de cartes/fond_carte_11.png").convert_alpha()
    fond_carte_pa = pygame.image.load("ressources/fonds de cartes/fond_carte_09.png").convert_alpha()

    continuer = True
    while continuer:
        # fond = pygame.image.load("ressources/images/background_gwent.jpg").convert()
        # screen.blit(fond, (0, 0))

        text_tools.draw_text(str(joueur2.hp), font_text, (0, 0, 0), screen, 460, 60)
        screen.blit(heart_small, (450, 20))
        text_tools.draw_text(str(joueur1.hp), font_text, (0, 0, 0), screen, 460, 870)
        screen.blit(heart_small, (450, 830))

        text_tools.draw_text(str(joueur2.shield), font_text, (0, 0, 0), screen, 535, 60)
        screen.blit(shield_small, (525, 20))
        text_tools.draw_text(str(joueur1.shield), font_text, (0, 0, 0), screen, 535, 870)
        screen.blit(shield_small, (525, 830))

        text_tools.draw_text(str(joueur2.mana_stock), font_text, (0, 0, 0), screen, 845, 60)
        text_tools.draw_text('(+' + str(joueur2.mana_generation) + ')', font_text, (0, 0, 0), screen, 860, 60)
        screen.blit(pm_small, (850, 20))
        text_tools.draw_text(str(joueur1.mana_stock), font_text, (0, 0, 0), screen, 845, 870)
        text_tools.draw_text('(+' + str(joueur1.mana_generation) + ')', font_text, (0, 0, 0), screen, 860, 870)
        screen.blit(pm_small, (850, 830))

        text_tools.draw_text(str(joueur2.gold_stock), font_text, (0, 0, 0), screen, 915, 60)
        text_tools.draw_text('(+' + str(joueur2.gold_generation) + ')', font_text, (0, 0, 0), screen, 935, 60)
        screen.blit(po_small, (925, 20))
        text_tools.draw_text(str(joueur1.gold_stock), font_text, (0, 0, 0), screen, 915, 870)
        text_tools.draw_text('(+' + str(joueur1.gold_generation) + ')', font_text, (0, 0, 0), screen, 935, 870)
        screen.blit(po_small, (925, 830))

        text_tools.draw_text(str(joueur2.action_stock), font_text, (0, 0, 0), screen, 990, 60)
        text_tools.draw_text('(+' + str(joueur2.action_generation) + ')', font_text, (0, 0, 0), screen, 1010, 60)
        screen.blit(pa_small, (1000, 20))
        text_tools.draw_text(str(joueur1.action_stock), font_text, (0, 0, 0), screen, 990, 870)
        text_tools.draw_text('(+' + str(joueur1.action_generation) + ')', font_text, (0, 0, 0), screen, 1010, 870)
        screen.blit(pa_small, (1000, 830))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer = False

        pygame.display.update()

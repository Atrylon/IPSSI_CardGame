import sys
import pygame
import random
from pygame.locals import *

import mysql_connexion
import text_tools

from Classes.Deck import Deck
from Classes.Player import Player
from Classes.Card import Card

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1280, 910))
font_title = pygame.font.SysFont('Helvetic', 75)
font_text = pygame.font.SysFont('Comic Sans MS,Arial', 15)
font_text_small = pygame.font.SysFont('Comic Sans MS', 12)

hand1 = {}
hand2 = {}

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

fond_carte_po = pygame.image.load("ressources/fonds de cartes/fond_carte_13.png").convert_alpha()
fond_carte_pm = pygame.image.load("ressources/fonds de cartes/fond_carte_11.png").convert_alpha()
fond_carte_pa = pygame.image.load("ressources/fonds de cartes/fond_carte_09.png").convert_alpha()


fond_carte_po_small = pygame.image.load("ressources/fonds de cartes/fond_carte_13_small.png").convert_alpha()
fond_carte_pm_small  = pygame.image.load("ressources/fonds de cartes/fond_carte_11_small.png").convert_alpha()
fond_carte_pa_small  = pygame.image.load("ressources/fonds de cartes/fond_carte_09_small.png").convert_alpha()


def game():
    cards = mysql_connexion.readCards()
    deck_joueur1 = Deck('Deck de test 1')
    deck_joueur2 = Deck('Deck de test 2')
    joueur1 = Player(1, 'Atrylon')
    joueur2 = Player(2, 'Ordinateur')

    for card in cards:
        deck_joueur1.add_card_to_deck(card)
        deck_joueur2.add_card_to_deck(card)

    # On remplit la main de départ des joueurs
    # Main du joueur1
    for i in range(0, 7):
        card_from_hand_to_deck = random.choice(deck_joueur1.get_cards_from_deck())
        card_to_add = Card(card_from_hand_to_deck[1],
                           card_from_hand_to_deck[2],
                           card_from_hand_to_deck[3],
                           card_from_hand_to_deck[4],
                           card_from_hand_to_deck[5],
                           card_from_hand_to_deck[6],
                           card_from_hand_to_deck[7],
                           card_from_hand_to_deck[8])
        joueur1.hand.append(card_to_add)
        deck_joueur1.del_card_from_deck(card_from_hand_to_deck)

    # Main du joueur2
    for j in range(0, 7):
        card_from_hand_to_deck2 = random.choice(deck_joueur2.get_cards_from_deck())
        card_to_add2 = Card(card_from_hand_to_deck2[1],
                            card_from_hand_to_deck2[2],
                            card_from_hand_to_deck2[3],
                            card_from_hand_to_deck2[4],
                            card_from_hand_to_deck2[5],
                            card_from_hand_to_deck2[6],
                            card_from_hand_to_deck2[7],
                            card_from_hand_to_deck2[8])
        joueur2.hand.append(card_to_add2)
        deck_joueur2.del_card_from_deck(card_from_hand_to_deck2)

    # print('cartes du deck :')
    # for card_in_deck in deck_joueur1.get_cards_from_deck():
    #     print(card)

    continuer = True
    while continuer:
        mx, my = pygame.mouse.get_pos()
        game_interface(joueur1, joueur2)
        print_hand(joueur1)
        print_hand(joueur2)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer = False
            if event.type == MOUSEBUTTONDOWN:
                for i in range(0, 6):
                    if hand1[i].collidepoint((mx, my)) and event.button == 1:
                        print('Clic sur la ' + str(i+1) + 'eme carte de ma main du joueur 1')
                        print(joueur1.hand[i].name)
                    if hand2[i].collidepoint((mx, my)) and event.button == 1:
                        print('Clic sur la ' + str(i+1) + 'eme carte de ma main du joueur 2')
                        print(joueur2.hand[i].name)
                #
                # if event.button == 1:
                #     print('clic gauche')
                # if event.button == 2:
                #     print('clic central')
                # if event.button == 3:
                #     print('clic droit')

        pygame.display.update()


def game_interface(joueur1, joueur2):
    screen.fill((192, 192, 192))
    rect_joueur_2 = pygame.Rect(10, 0, 1260, 100)
    pygame.draw.rect(screen, (0, 0, 0), rect_joueur_2, 25)
    text_tools.draw_text(joueur2.name, font_title, (0, 0, 0), screen, 35, 25)

    rect_joueur_1 = pygame.Rect(10, 810, 1260, 100)
    pygame.draw.rect(screen, (0, 0, 0), rect_joueur_1, 25)
    text_tools.draw_text(joueur1.name, font_title, (0, 0, 0), screen, 35, 835)

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


def print_hand(joueur):
    position = joueur.get_player_index()
    player_hand = joueur.get_player_hand()
    global hand1
    global hand2

    if position == 1:
        x = 50
        y = 580

        for i in range(0, 6):
            hand1[i] = pygame.Rect(x, y, 150, 200)
            pygame.draw.rect(screen, (192, 192, 192), hand1[i])

            text_tools.draw_text("Coût :", font_text, (0, 0, 0), screen, x+15, y+50)
            text_tools.draw_text(str(player_hand[i].cost), font_text, (0, 0, 0), screen, x+67, y+50)
            if player_hand[i].ressource_type == 'PA':
                screen.blit(fond_carte_pa_small, (x, y))
                screen.blit(pa_very_small, (x+105, y+52))
            elif player_hand[i].ressource_type == 'PO':
                screen.blit(fond_carte_po_small, (x, y))
                screen.blit(po_very_small, (x+105, y+52))
            elif player_hand[i].ressource_type == 'PM':
                screen.blit(fond_carte_pm_small, (x, y))
                screen.blit(pm_very_small, (x+105, y+52))

            text_tools.draw_text(player_hand[i].name, font_text_small, (0, 0, 0), screen, x+12, y+5)

            text_tools.draw_text(player_hand[i].target, font_text, (0, 0, 0), screen, x+15, y+100)
            text_tools.draw_text(str(player_hand[i].value), font_text, (0, 0, 0), screen, x+67, y+100)
            if player_hand[i].effect == 'Shield':
                screen.blit(shield_very_small, (x+105, y+102))
            elif player_hand[i].effect == 'Life':
                screen.blit(heart_very_small, (x+105, y+102))

            x += 175

    elif position == 2:
        x = 50
        y = 125

        for i in range(0, 6):
            hand2[i] = pygame.Rect(x, y, 150, 200)
            pygame.draw.rect(screen, (192, 192, 192), hand2[i])

            text_tools.draw_text("Coût :", font_text, (0, 0, 0), screen, x + 15, y + 50)
            text_tools.draw_text(str(player_hand[i].cost), font_text, (0, 0, 0), screen, x + 67, y + 50)
            if player_hand[i].ressource_type == 'PA':
                screen.blit(fond_carte_pa_small, (x, y))
                screen.blit(pa_very_small, (x + 105, y + 52))
            elif player_hand[i].ressource_type == 'PO':
                screen.blit(fond_carte_po_small, (x, y))
                screen.blit(po_very_small, (x + 105, y + 52))
            elif player_hand[i].ressource_type == 'PM':
                screen.blit(fond_carte_pm_small, (x, y))
                screen.blit(pm_very_small, (x + 105, y + 52))

            text_tools.draw_text(player_hand[i].name, font_text_small, (0, 0, 0), screen, x+12, y+5)

            text_tools.draw_text(player_hand[i].target, font_text, (0, 0, 0), screen, x + 15, y + 100)
            text_tools.draw_text(str(player_hand[i].value), font_text, (0, 0, 0), screen, x + 67, y + 100)
            if player_hand[i].effect == 'Shield':
                screen.blit(shield_very_small, (x + 105, y + 102))
            elif player_hand[i].effect == 'Life':
                screen.blit(heart_very_small, (x + 105, y + 102))

            x += 175
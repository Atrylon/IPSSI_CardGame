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

joueur1 = Player(1, '')
joueur2 = Player(2, 'Ordinateur')

deck_list_cards = Deck('Liste de toutes les cartes')
deck_joueur1 = Deck('Deck de test 1')
deck_joueur2 = Deck('Deck de test 2')
hand1 = {}
hand2 = {}
player1_username = ''
rect_end_turn = None
tour = None
deck_len = 32

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

fond_carte_po = pygame.image.load("ressources/fonds de cartes/fond_carte_13.png").convert_alpha()
fond_carte_pm = pygame.image.load("ressources/fonds de cartes/fond_carte_11.png").convert_alpha()
fond_carte_pa = pygame.image.load("ressources/fonds de cartes/fond_carte_09.png").convert_alpha()


fond_carte_po_small = pygame.image.load("ressources/fonds de cartes/fond_carte_13_small.png").convert_alpha()
fond_carte_pm_small = pygame.image.load("ressources/fonds de cartes/fond_carte_11_small.png").convert_alpha()
fond_carte_pa_small = pygame.image.load("ressources/fonds de cartes/fond_carte_09_small.png").convert_alpha()


def game():
    global joueur1
    global joueur2
    global tour
    global deck_joueur1
    global deck_joueur2
    global deck_list_cards

    def add_card_to_hand(deck, joueur, delete=False):
        card_from_hand_to_deck = random.choice(deck.get_cards_from_deck())
        card_to_add = Card(card_from_hand_to_deck[1],
                           card_from_hand_to_deck[2],
                           card_from_hand_to_deck[3],
                           card_from_hand_to_deck[4],
                           card_from_hand_to_deck[5],
                           card_from_hand_to_deck[6],
                           card_from_hand_to_deck[7],
                           card_from_hand_to_deck[8])
        joueur.hand.append(card_to_add)

        if delete :
            deck.del_card_from_deck(card_from_hand_to_deck)

    get_username()

    joueur1.change_name(player1_username)
    joueur1.add_action_to_stock()
    joueur1.add_gold_to_stock()
    joueur1.add_mana_to_stock()

    cards = mysql_connexion.readCards()

    for card in cards:
        deck_list_cards.add_card_to_deck(card)

    for i in range(0, deck_len):
        card_from_list_to_deck = random.choice(deck_list_cards.get_cards_from_deck())
        deck_joueur1.add_card_to_deck(card_from_list_to_deck)

        card_from_list_to_deck2 = random.choice(deck_list_cards.get_cards_from_deck())
        deck_joueur2.add_card_to_deck(card_from_list_to_deck2)

    tour = 1

    # On remplit la main de départ des joueurs
    # Main du joueur1
    for i in range(0, 7):
        add_card_to_hand(deck_joueur1, joueur1)
        # deck_joueur1.del_card_from_deck(card_from_hand_to_deck)

    # Main du joueur2
    for j in range(0, 7):
        add_card_to_hand(deck_joueur2, joueur2)

    print(str(deck_joueur1.get_nb_cards_in_deck()) + ' cartes dans le deck - Liste des cartes du deck :')
    for card_in_deck in deck_joueur1.get_cards_from_deck():
        print(card_in_deck)

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

                if tour % 2 == 1:
                    for i in range(0, len(joueur1.get_player_hand())):
                        # On joue la carte avec le bouton gauche
                        if hand1[i].collidepoint((mx, my)) and event.button == 1 and joueur1.hand[i]:
                            if joueur1.hand[i].ressource_type == 'PA':
                                if joueur1.action_stock >= joueur1.hand[i].cost:
                                    print('Vous pouvez jouer la carte')
                                else:
                                    print('Pas assez de ressouces')
                            elif joueur1.hand[i].ressource_type == 'PM':
                                if joueur1.mana_stock >= joueur1.hand[i].cost:
                                    print('Vous pouvez jouer la carte')
                                else:
                                    print('Pas assez de ressouces')
                            elif joueur1.hand[i].ressource_type == 'PO':
                                if joueur1.gold_stock >= joueur1.hand[i].cost:
                                    print('Vous pouvez jouer la carte')
                                else:
                                    print('Pas assez de ressouces')

                                # print()
                                # joueur1.hand.remove(joueur1.hand[i])

                        # Discard avec le bouton droit
                        elif hand1[i].collidepoint((mx, my)) and event.button == 3 and joueur1.hand[i]:
                            print('Clic sur la ' + str(i+1) + 'eme carte de ma main du joueur 1')
                            print('discard ' + joueur1.hand[i].name)
                            joueur1.hand.remove(joueur1.hand[i])

                            if deck_joueur1.get_nb_cards_in_deck() > 0:
                                add_card_to_hand(deck_joueur1, joueur1, True)

                elif tour % 2 == 0:
                    for j in range(0, len(joueur2.get_player_hand())):
                        # On joue la carte avec le bouton gauche
                        if hand2[j].collidepoint((mx, my)) and event.button == 1 and joueur2.hand[j]:
                            if joueur2.hand[j].ressource_type == 'PA':
                                if joueur2.action_stock >= joueur2.hand[i].cost:
                                    print('Vous pouvez jouer la carte')
                                else:
                                    print('Pas assez de ressouces')
                            elif joueur2.hand[j].ressource_type == 'PM':
                                if joueur2.mana_stock >= joueur2.hand[i].cost:
                                    print('Vous pouvez jouer la carte')
                                else:
                                    print('Pas assez de ressouces')
                            elif joueur2.hand[j].ressource_type == 'PO':
                                if joueur2.gold_stock >= joueur2.hand[i].cost:
                                    print('Vous pouvez jouer la carte')
                                else:
                                    print('Pas assez de ressouces')
                            # joueur2.hand.remove(joueur2.hand[j])

                        # Discard avec le bouton droit
                        elif hand2[j].collidepoint((mx, my)) and event.button == 3 and joueur2.hand[j]:
                            print('Clic sur la ' + str(j+1) + 'eme carte de ma main du joueur 2')
                            print('discard ' + joueur2.hand[j].name)
                            joueur2.hand.remove(joueur2.hand[j])

                            if deck_joueur2.get_nb_cards_in_deck() > 0:
                                add_card_to_hand(deck_joueur2, joueur2, True)

                if rect_end_turn.collidepoint((mx, my)) and event.button == 1:
                    print('Fin du tour')
                    print('Tour ' + str(tour))

                    if tour % 2 == 0:
                        joueur1.add_action_to_stock()
                        joueur1.add_gold_to_stock()
                        joueur1.add_mana_to_stock()
                    elif tour % 2 == 1:
                        joueur2.add_action_to_stock()
                        joueur2.add_gold_to_stock()
                        joueur2.add_mana_to_stock()

                    tour += 1

        pygame.display.update()


def game_interface(joueur1, joueur2):
    screen.fill((192, 192, 192))
    global rect_end_turn

    rect_joueur_2 = pygame.Rect(10, 0, 1260, 100)
    pygame.draw.rect(screen, (0, 0, 0), rect_joueur_2, 25)
    text_tools.draw_text(joueur2.name, font_title, (0, 0, 0), screen, 35, 25)

    rect_joueur_1 = pygame.Rect(10, 810, 1260, 100)
    pygame.draw.rect(screen, (0, 0, 0), rect_joueur_1, 25)
    text_tools.draw_text(joueur1.name, font_title, (0, 0, 0), screen, 35, 835)

    text_tools.draw_text('Tour ' + str(tour), font_text, (0, 0, 0), screen, 25, 440)

    rect_end_turn = pygame.Rect(1140, 425, 100, 50)
    pygame.draw.rect(screen, (0, 0, 0), rect_end_turn, 10)
    text_tools.draw_text('Fin de tour', font_text, (0, 0, 0), screen, 1155, 440)

    text_tools.draw_text(str(joueur2.hp), font_text, (0, 0, 0), screen, 460, 60)
    screen.blit(heart_small, (450, 20))
    text_tools.draw_text(str(joueur1.hp), font_text, (0, 0, 0), screen, 460, 870)
    screen.blit(heart_small, (450, 830))

    text_tools.draw_text(str(joueur2.shield), font_text, (0, 0, 0), screen, 535, 60)
    screen.blit(shield_small, (525, 20))
    text_tools.draw_text(str(joueur1.shield), font_text, (0, 0, 0), screen, 535, 870)
    screen.blit(shield_small, (525, 830))

    text_tools.draw_text(str(joueur2.mana_stock), font_text, (0, 0, 0), screen, 745, 60)
    text_tools.draw_text('(+' + str(joueur2.mana_generation) + ')', font_text, (0, 0, 0), screen, 760, 60)
    screen.blit(pm_small, (750, 20))
    text_tools.draw_text(str(joueur1.mana_stock), font_text, (0, 0, 0), screen, 745, 870)
    text_tools.draw_text('(+' + str(joueur1.mana_generation) + ')', font_text, (0, 0, 0), screen, 760, 870)
    screen.blit(pm_small, (750, 830))

    text_tools.draw_text(str(joueur2.gold_stock), font_text, (0, 0, 0), screen, 815, 60)
    text_tools.draw_text('(+' + str(joueur2.gold_generation) + ')', font_text, (0, 0, 0), screen, 835, 60)
    screen.blit(po_small, (825, 20))
    text_tools.draw_text(str(joueur1.gold_stock), font_text, (0, 0, 0), screen, 815, 870)
    text_tools.draw_text('(+' + str(joueur1.gold_generation) + ')', font_text, (0, 0, 0), screen, 835, 870)
    screen.blit(po_small, (825, 830))

    text_tools.draw_text(str(joueur2.action_stock), font_text, (0, 0, 0), screen, 890, 60)
    text_tools.draw_text('(+' + str(joueur2.action_generation) + ')', font_text, (0, 0, 0), screen, 910, 60)
    screen.blit(pa_small, (900, 20))
    text_tools.draw_text(str(joueur1.action_stock), font_text, (0, 0, 0), screen, 890, 870)
    text_tools.draw_text('(+' + str(joueur1.action_generation) + ')', font_text, (0, 0, 0), screen, 910, 870)
    screen.blit(pa_small, (900, 830))

    text_tools.draw_text(str(deck_joueur2.get_nb_cards_in_deck()) + ' card(s) left', font_text, (0, 0, 0), screen, 1100,
                         60)
    screen.blit(deck_small, (1120, 20))
    text_tools.draw_text(str(deck_joueur1.get_nb_cards_in_deck()) + ' card(s) left', font_text, (0, 0, 0), screen, 1100,
                         870)
    screen.blit(deck_small, (1120, 830))


def print_hand(joueur):
    position = joueur.get_player_index()
    player_hand = joueur.get_player_hand()
    global hand1
    global hand2

    if position == 1:
        x = 50
        y = 580

        for i in range(0, len(joueur.get_player_hand())):
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

        for i in range(0, len(joueur.get_player_hand())):
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


def get_username():
    font = pygame.font.Font(None, 70)
    input_box = pygame.Rect(400, 445, 350, 65)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    global player1_username
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        player1_username = text
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        text_tools.draw_text("Votre pseudo :", font, pygame.Color('dodgerblue2'), screen, 50, 455)
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(350, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
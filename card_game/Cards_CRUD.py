import sys
import pygame
from pygame.locals import *

import text_tools, mysql_connexion

screen = pygame.display.set_mode((1280, 910))
card_cadre = pygame.display.set_mode((275, 350))
# font_text = pygame.font.SysFont('Comic Sans MS', 20)


def cards_list():
    font_text = pygame.font.SysFont('Comic Sans MS,Arial', 20)
    font_title = pygame.font.SysFont('Helvetic', 75)

    continuer = True
    card_set = {}

    # begin of the loop
    n = 0
    # end of the loop
    m = 3

    while continuer:
        mx, my = pygame.mouse.get_pos()
        screen.fill((192, 192, 192))

        button_option_1 = pygame.Rect(20, 20, 100, 40)
        pygame.draw.rect(screen, (0, 0, 0), button_option_1)
        text_tools.draw_text('Retour', font_text, (255, 255, 255), screen, 35, 25)

        cards = mysql_connexion.readCards()
        nb_cards = len(cards)

        fond_carte_po = pygame.image.load("ressources/fonds de cartes/fond_carte_13.png").convert_alpha()
        fond_carte_pm = pygame.image.load("ressources/fonds de cartes/fond_carte_11.png").convert_alpha()
        fond_carte_pa = pygame.image.load("ressources/fonds de cartes/fond_carte_09.png").convert_alpha()

        left_arrow = pygame.image.load("ressources/images/left arrow.png").convert_alpha()
        left_arrow_small = pygame.transform.scale(left_arrow, (50, 50))
        button_left_arrow = pygame.Rect(5, 430, 50, 50)
        pygame.draw.rect(screen, (192, 192, 192), button_left_arrow)

        right_arrow = pygame.image.load("ressources/images/right arrow.png").convert_alpha()
        right_arrow_small = pygame.transform.scale(right_arrow, (50, 50))
        button_right_arrow = pygame.Rect(1225, 430, 50, 50)
        pygame.draw.rect(screen, (192, 192, 192), button_right_arrow)

        x = 110
        y = 200

        # On veut afficher juste 3 cartes à la fois
        for card in cards[n:m]:

            # card_set[card[0]] = pygame.Rect(x, y, 340, 474)
            # pygame.draw.rect(screen, (192, 192, 192), card_set[card[0]])

            if card[2] == "PO":
                screen.blit(fond_carte_po, (x, y))
            elif card[2] == "PM":
                screen.blit(fond_carte_pm, (x, y))
            elif card[2] == "PA":
                screen.blit(fond_carte_pa, (x, y))

            if n > 0:
                screen.blit(left_arrow_small, (5, 430))
            if nb_cards > n+3:
                screen.blit(right_arrow_small, (1225, 430))

            text_tools.draw_text(card[1], font_text, (0, 0, 0), screen, x + 50, y + 20)
            text_tools.draw_text('Cost : ' + str(card[3]) + ' ' + card[2], font_text, (0, 0, 0), screen, x + 50, y + 100)
            text_tools.draw_text('Effect : ' + str(card[5]) + ' ' + card[6] + ' ' + card[4], font_text, (0, 0, 0), screen, x + 50, y + 175)
            text_tools.draw_text('Rarity : ' + card[7], font_text, (0, 0, 0), screen, x + 50, y + 250)

            # text_tools.blit_text(card_cadre, card[8], (x+50, y+100), font_text)

            x += 350

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

                # for i in range(n, m):
                #     if card_set[i+1].collidepoint(mx, my) and event.button == 1:
                #         print(card_set[i+1])

                if button_left_arrow.collidepoint(mx, my) and event.button == 1 and n > 0:
                    n = n - 3
                    m = m - 3
                elif button_right_arrow.collidepoint(mx, my) and event.button == 1 and nb_cards > n+3:
                    n = n + 3
                    m = m + 3

        pygame.display.update()

import sys
import pygame
from pygame.locals import *

import mysql_connexion
import text_tools

screen = pygame.display.set_mode((1280, 910))
card_cadre = pygame.display.set_mode((275, 350))
# font_text = pygame.font.SysFont('Comic Sans MS', 20)


def cards_list():
    font_text = pygame.font.SysFont('Comic Sans MS,Arial', 20)
    font_title = pygame.font.SysFont('Helvetic', 75)

    continuer = True
    click = False
    cards_set = 0
    cards_in_set = 0

    while continuer:
        mx, my = pygame.mouse.get_pos()
        screen.fill((192, 192, 192))

        button_option_1 = pygame.Rect(20, 20, 100, 40)

        pygame.draw.rect(screen, (255, 0, 0), button_option_1)

        text_tools.draw_text('Retour', font_text, (0, 0, 0), screen, 35, 25)

        cards = mysql_connexion.readCards()

        fond_carte_po = pygame.image.load("ressources/fonds de cartes/fond_carte_13.png").convert_alpha()
        fond_carte_pm = pygame.image.load("ressources/fonds de cartes/fond_carte_11.png").convert_alpha()
        fond_carte_pa = pygame.image.load("ressources/fonds de cartes/fond_carte_09.png").convert_alpha()
        left_arrow = pygame.image.load("ressources/images/left arrow.png").convert_alpha()
        left_arrow_small = pygame.transform.scale(left_arrow, (50, 50))
        right_arrow = pygame.image.load("ressources/images/right arrow.png").convert_alpha()
        right_arrow_small = pygame.transform.scale(right_arrow, (50, 50))
        x = 110
        y = 200

        for card in cards:
            # if cards_in_set == 3:
            #     break

            if card[2] == "PO":
                screen.blit(fond_carte_po, (x, y))
            elif card[2] == "PM":
                screen.blit(fond_carte_pm, (x, y))
            elif card[2] == "PA":
                screen.blit(fond_carte_pa, (x, y))
            cards_in_set += 1

            if cards_set != 0:
                screen.blit(left_arrow_small, (5, 430))
            screen.blit(right_arrow_small, (1225, 430))

            text_tools.draw_text(card[1], font_text, (0, 0, 0), screen, x+50, y+20)
            text_tools.draw_text('Cost : ' + str(card[3]) + ' ' + card[2], font_text, (0, 0, 0), screen, x+50, y+100)
            text_tools.draw_text('Effect : ' + str(card[5]) + ' ' + card[6] + ' ' + card[4], font_text, (0, 0, 0), screen, x+50, y+175)
            text_tools.draw_text('Rarity : ' + card[7], font_text, (0, 0, 0), screen, x+50, y+250)

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

                if left_arrow_small.get_rect().collidepoint(mx, my):
                   print("clic")
                if left_arrow_small.get_rect().collidepoint(mx, my):
                    cards_set -= 1
                    print(cards_set)
                elif right_arrow_small.get_rect().collidepoint(mx, my):
                    cards_set += 1
                    print(cards_set)

        pygame.display.update()
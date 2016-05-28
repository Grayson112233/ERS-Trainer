# Random walker program by Grayson Pike
# Originally written December 2014
# Rewritten May 2016
# No controls, press escape to close window

import pygame
from cards import Card, is_double_or_sandwich, get_random_card
import globals

from display import toggle_fullscreen

globals.WIDTH = 500
globals.HEIGHT = 726
globals.fullscreen = False

rank_filenames = [
    '2', '3', '4', '5', '6', '7', '8', '9',
    '10', 'jack', 'queen', 'king', 'ace'
]

suit_filenames = [
    "hearts", "spades", "clubs", "diamonds"
]

card_images = []
cards = [get_random_card(), Card(0, 0), Card(0, 0)]


def load_cards():
    for i in range(4):
        ranks = []
        for j in range(13):
            ranks.append(pygame.image.load("res/" + rank_filenames[j] + "_of_" + suit_filenames[i] + ".png"))
        card_images.append(ranks)


def new_card():
    cards[2].copy(cards[1])
    cards[1].copy(cards[0])
    cards[0] = get_random_card()
    # print("Printing card with suit " + str(cards[0].suit) + " and rank " + str(cards[0].rank) + ".")
    globals.window.blit(card_images[cards[0].suit][cards[0].rank], (0, 0))


def main():

    # Initialize pygame
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    globals.window = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT), False)

    sound_correct = pygame.mixer.Sound("res/correct.wav")
    sound_incorrect = pygame.mixer.Sound("res/incorrect.wav")

    load_cards()
    loop = True
    timer = 1
    space_pressed = False
    score = 0

    while(loop):

        clock.tick(60)

        timer += 1
        if timer >= 50:
            timer = 0
            new_card()
            space_pressed = False

        # Check if the escape key has been pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    if(is_double_or_sandwich(cards) and not space_pressed):
                        score += 1
                        print("Correct: Score is " + str(score))
                        space_pressed = True
                        sound_correct.play()
                    elif(not space_pressed):
                        score -= 1
                        print("Incorrect: Score is " + str(score))
                        space_pressed = True
                        sound_incorrect.play()

                if event.key == pygame.K_RETURN:
                    toggle_fullscreen()

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.flip()


main()

from random import randint


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def print_card(self):
        print("<Suit=" + str(self.suit) + ", rank=" + str(self.rank) + ">")

    def equals_rank(self, card):
        if(self.rank == card.rank):
            return True
        return False

    def copy(self, card):
        self.suit = card.suit
        self.rank = card.rank


def is_double_or_sandwich(cards):

    # print("testing for double:")
    cards[0].print_card()
    cards[1].print_card()
    cards[2].print_card()

    # Double
    if(cards[0].equals_rank(cards[1])):
        return True

    # Sandwich
    if(cards[0].equals_rank(cards[2])):
        return True

    return False


def get_random_card():
    suit = randint(0, 3)
    rank = randint(0, 12)
    return Card(suit, rank)

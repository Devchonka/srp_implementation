"""
Elena Menyaylenko
Homework #5
10/30/15


Objectives:          Develop an object oriented program to create a Card class
                    Develop a test program that is separate from the class under development

"""
from random import randint

# Two dictionaries that allow lookup for the __str__ method.
rank_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven',
             8: 'Eight', 9: 'Nine', 10: 'Jack', 11: 'Queen', 12: 'King', 13: 'Ace'}
suit_dict = {'d': 'Diamonds', 's': 'Spades', 'h': 'Hearts', 'c': 'Clubs'}


class Card:
    """
    Card class to allow creation of card objects with a specified rank and suit.
    The Card object represents a card which has a rank 1-13, the last four being face cards, and one
    of the four suits in the typical French card deck.
    """

    def __init__(self, rank, suit):
        """
        rank is a number in the range 1-13 indicating the ranks Ace through King.
        suit is a single character "d" "c", "h", or "s" indicating the suit
        (diamonds, clubs, hearts, or spades).
        """
        self.rank = rank
        self.suit = suit

    def getRank(self):
        """
        Function returns the rank of the card instance.
        """
        return self.rank

    def getSuit(self):
        """
        Function returns the suit of the card instance.
        """
        return self.suit

    def bjValue(self):
        """
        Function returns the Blackjack value of a card. Ace counts as 1, face cards count as 10.
        """
        if self.rank > 9:  # face card
            return 10
        else:
            return self.rank

    def __str__(self):
        """
        Function returns a string that names the card. For example. "Ace of Spades".
        """
        return str(rank_dict[self.getRank()] + ' of ' + suit_dict[self.getSuit()])


class CardTester:
    """
    This is a test class which contains abilities to test all functions of interest in Card class.
    """
    def __init__(self):
        """
        Instantiation of the class. Creates a card stack initialized as None.
        """
        self.card_stack = None
        print("Card Tester instance created to test out several card instances.")
    def create_cards(self, nCards):
        """
        A method that creates some amount of random cards specified by the user.
        :param nCards: the number of cards that the user wants created
        :return:fills up the self.card_stack in the class
        """
        possible_suits = ["d", "c", "h", "s"]
        if self.card_stack == None:
            self.card_stack = []
        else:
            self.card_stack = []
        for card in range(nCards):
            random_rank = randint(1, 13)
            random_suit = possible_suits[randint(0, 3)]
            self.card_stack.append(Card(random_rank, random_suit))

    def show_created_cards(self):
        """
        This method prints to the screen all the cards that were randomly created.
        :return: Does not return values, only prints card rank and suit to screen.
        """
        print('\nShowing created cards.')
        if self.card_stack is not None:
            for card_num, card in enumerate(self.card_stack):
                print(
                    'Card number {} generated rank {} and suit {}'.format(card_num + 1, card.getRank(), card.getSuit()))
        else:
            print('No cards created!')

    def test_bjValues(self):
        """
        Method that prints to the screen the black jack values of each card tested.
        :return: No returned values, cards black jack values are printed to screen.
        """
        print('\nTesting black jack values of cards.')
        if self.card_stack is not None:
            for card_num, card in enumerate(self.card_stack):
                print('Card number {} has black jack value {}'.format(card_num + 1, card.bjValue()))
        else:
            print('No cards created!')

    def test_str_of_cards(self):
        """
        Method tests __str__ method for Card class.
        :return: No returned values, Simply prints card's called __str__ to screen.
        """
        print('\nTesting str function of cards.')
        if self.card_stack is not None:
            for card_num, card in enumerate(self.card_stack):
                print('Card number {} is written as {}'.format(card_num + 1, card))
        else:
            print('No cards created!')


def main():
    """
    Function that allows user to create one card or use the test class to create any number of cards for testing.
    """
    new_card = Card(12, 'c')
    print(new_card)

    card_tester = CardTester()
    card_tester.create_cards(3)
    card_tester.show_created_cards()
    card_tester.test_bjValues()
    card_tester.test_str_of_cards()


if __name__ == '__main__':
    main()

""" OUTPUT:
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hwk5 $ python3 main.py
King of Clubs
Card Tester instance created to test out several card instances.

Showing created cards.
Card number 1 generated rank 5 and suit c
Card number 2 generated rank 13 and suit h
Card number 3 generated rank 3 and suit c

Testing black jack values of cards.
Card number 1 has black jack value 5
Card number 2 has black jack value 10
Card number 3 has black jack value 3

Testing str function of cards.
Card number 1 is written as Five of Clubs
Card number 2 is written as Ace of Hearts
Card number 3 is written as Three of Clubs
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hwk5 $ python3 main.py
King of Clubs
Card Tester instance created to test out several card instances.

Showing created cards.
Card number 1 generated rank 10 and suit c
Card number 2 generated rank 3 and suit s
Card number 3 generated rank 5 and suit s

Testing black jack values of cards.
Card number 1 has black jack value 10
Card number 2 has black jack value 3
Card number 3 has black jack value 5

Testing str function of cards.
Card number 1 is written as Jack of Clubs
Card number 2 is written as Three of Spades
Card number 3 is written as Five of Spades
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hwk5 $ python3 main.py
King of Clubs
Card Tester instance created to test out several card instances.

Showing created cards.
Card number 1 generated rank 10 and suit c
Card number 2 generated rank 7 and suit d
Card number 3 generated rank 9 and suit d

Testing black jack values of cards.
Card number 1 has black jack value 10
Card number 2 has black jack value 7
Card number 3 has black jack value 9

Testing str function of cards.
Card number 1 is written as Jack of Clubs
Card number 2 is written as Seven of Diamonds
Card number 3 is written as Nine of Diamonds
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hwk5 $

"""
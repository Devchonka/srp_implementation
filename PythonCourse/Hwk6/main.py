"""
11/04/15
Elena Menyaylenko
Hwk 6

Objective:       Raising and excepting errors in a robust class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hints:

• Solve each of the four problems above one at a time, but perform all tests each time to make sure
that code that solves one of the problems doesn't break your solution to one of the previous problems.

"""

from random import randint


class Card:
    """
    Card class to allow creation of card objects with a specified rank and suit.
    The Card object represents a card which has a rank 1-13, the last four being face cards, and one
    of the four suits in the typical French card deck.
    """
    # Two dictionaries that allow lookup for the __str__ method.
    rank_dict = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven',
                 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King'}
    suit_dict = {'d': 'Diamonds', 's': 'Spades', 'h': 'Hearts', 'c': 'Clubs'}

    def __init__(self, rank, suit):
        """
        rank is a number in the range 1-13 indicating the ranks Ace through King.
        suit is a single character "d" "c", "h", or "s" indicating the suit
        (diamonds, clubs, hearts, or spades).

        This instantiator will raise exceptions base on one of the 4 things:
        1) TypeError when the type of the first parameter is not an int.
        2) TypeError when the type of the second parameter is not a string.
        3) ValueError when the value of the first parameter is not in the range 1..13 inclusive.
        4) ValueError when the value of the second parameter is not one of the strings in the set {'s', 'h', 'c', 'd'}
        """
        if type(rank) != int:
            raise TypeError()
        if type(suit) != str:
            raise TypeError()
        if rank not in range(1, 14):
            raise ValueError()
        if suit not in list('shcd'):
            raise ValueError()

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
        if self.rank > 10 or self.rank == 1:  # face card
            return 10
        else:
            return self.rank

    def __str__(self):
        """
        Function returns a string that names the card. For example. "Ace of Spades".
        """
        return str(Card.rank_dict[self.getRank()] + ' of ' + Card.suit_dict[self.getSuit()])


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
    card_1 = attempt_create_card(-14, 3)
    card_2 = attempt_create_card(12, 'd')
    card_3 = attempt_create_card(11, 'a')
    card_4 = attempt_create_card('a', 12)
    card_5 = attempt_create_card(11, 11)

    # card_tester = CardTester()
    # card_tester.create_cards(3)
    # card_tester.show_created_cards()
    # card_tester.test_bjValues()
    # card_tester.test_str_of_cards()


def attempt_create_card(rank, suit):
    new_card = None
    try:
        new_card = Card(rank, suit)
    except TypeError:
        print('Type Error: The first parameter must be an int, second a string')
    except ValueError:
        print('Value Error: The value of the first parameter must lay in range [1,13] and '
              'second parameter be one of the letters "c", "d", "h", or "s"')
    else:
        print('Card has black jack value {}'.format(new_card.bjValue()))
        print(new_card)
    finally:
        print('Finished with card.\n')
    return new_card


if __name__ == '__main__':
    main()

""" OUTPUT:
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hwk6 $ python3 main.py
Type Error: The first parameter must be an int, second a string
Finished with card.

Card has black jack value 10
Queen of Diamonds
Finished with card.

Value Error: The value of the first parameter must lay in range [1,13] and second parameter be one of the letters "c", "d", "h", or "s"
Finished with card.

Type Error: The first parameter must be an int, second a string
Finished with card.

Type Error: The first parameter must be an int, second a string
Finished with card.

elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hwk6 $
"""
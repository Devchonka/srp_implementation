
"""
10/08/15
Homework 2
Elena Menyaylenko

Topic: Tuples and Lists

Objective: To write a program that prints form letters asking for votes in upcoming election.

Objectives:       Use tuples and lists
                        Format a form letter
                        Document your program
                        Print out both the program and the output to turn in.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def main():
    """
    This is the main function that will contain the collection of strings to print the letter.
    """
    (addressees, candidates, senders) = get_names()
    # Create a template for the letter using line by line separately
    letter_collection = []
    for x in range(3):
        intro_line = 'Dear %s, \n\n' % addressees[x]
        purpose_line = 'I would like you to vote for %s \n because I think ' \
                       'they are best for this state. \n\n' % candidates[x]
        regards_line = 'Cheers,\n\n %s\n\n' % senders[x]
        letter_collection.append([intro_line, purpose_line, regards_line])

    print_all_letters(letter_collection)


def print_all_letters(my_letters):
    """
    The function will print out a formatted statement of any number of provided letters.
    :param my_letters: An iterable collection of letters to be printed by this function
    :return: printed statement of formatted letters
    """
    [print(''.join(my_letters[x])) for x in range(len(my_letters))]

def get_names():
    """
    Function that allows to input the relevant names of addressees, candidates, and senders
    :return: returns a list of relevant names
    """
    possible_dem_candidates = ['Joe Biden', 'Hillary Clinton', 'Bernie Sanders']
    addressees = ("Joanna", "Mary", "Kaitlyn")
    candidates = (possible_dem_candidates[0], possible_dem_candidates[0], possible_dem_candidates[2])
    senders = ['Justin', 'Kristin', 'Sarah']
    return (addressees, candidates, senders)


if __name__== "__main__":
    main()

#     Program Output:
#     Dear Joanna,
#
# I would like you to vote for Joe Biden
#  because I think they are best for this state.
#
# Cheers,
#
#  Justin
#
#
# Dear Mary,
#
# I would like you to vote for Joe Biden
#  because I think they are best for this state.
#
# Cheers,
#
#  Kristin
#
#
# Dear Kaitlyn,
#
# I would like you to vote for Bernie Sanders
#  because I think they are best for this state.
#
# Cheers,
#
#  Sarah
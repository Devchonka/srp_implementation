"""
Elena Menyaylenko
10/23/2015
Homework #4

Objective:   Decompose spelling of a number to separate functions.

Run program from terminal (example): python3 main.py -564223

"""
#!/usr/bin/python

import sys
from math import floor

# bad: global variables
nums = ['one', 'two', 'three', 'four', 'five',
                              'six', 'seven', 'eight', 'nine', 'ten',
                              'eleven', 'twelve', 'thirteen', 'fourteen',
                              'fifteen', 'sixteen', 'seventeen',
                              'eighteen', 'nineteen']
tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
              'eighty', 'ninety']

def main():
    """
    This function is simply there to be an interface to collect system parameters,
    for convenience of naming it main()
    :return: Simply calls the spell() function
    """
    number = int(sys.argv[1])
    spell(number)

def spell(num):
    """
    Main function that returns the spelling of a number of anywhere in the millions or less, positive or negative.
    :param num: input number from the user (terminal)
    :return: returns the spelling of the input number to the screen
    """
    if num < 0:
        pre_pend = "negative "
        num = -num
    else:
        pre_pend =""

    chunks = split_to_chunks(num)
    chunks_len = len(chunks)
    hundr_string = thou_string = mill_string = ""

    mid = [""]
    if chunks_len ==2:
        mid = [" thousand "]
    elif chunks_len ==3:
        mid = [" million ", " thousand "]

    if chunks_len > 0:
        mill_string = spell_3digit_num(chunks[0])
    if chunks_len > 1:
        thou_string = mid[0] + spell_3digit_num(chunks[1])
    if chunks_len > 2:
        hundr_string = mid[1] + spell_3digit_num(chunks[2])

    word_string = "".join([pre_pend, mill_string, thou_string, hundr_string])
    print(word_string)

def split_to_chunks(num):
    """
    Function that splits a large number into separate 3-digit chunks.
    :param num: int input parameter which is a large number -999,999,999 - 999,999,999
    :return: returns a list of num broken down to 3-digit pieces at most in the correct order
            (million, thousand, hundred)
    """
    chunks = [] # hundredths, thousandths, millionths
    while num>999:
        chunks.append(num % 1e3)
        num = floor(num/1e3)
    chunks.append(num)
    return chunks[::-1]

def split_num(num, right_chunk_len):
    """
    This function splits a 2 or 3-digit number into 2 smaller numbers, specified by right_chunk_len
    :param num: input larger number to be split for further processing
    :param right_chunk_len: the size of the large number (number of digits on the right)
    :return: returns the right and left bits of the split number as a tuple
    """
    right_result = int(num % 10**right_chunk_len)
    left_result = floor(num / 10**right_chunk_len)
    return right_result, left_result

def get20to100(num):
    """
    Returns the spelling of any hundredths number, distinguishing to less than 20 and
    greater than 20 but less than 100
    :param num: input 2 digit number
    :return: Returns a complete string and the possibility of a right and left split, for larger (2 digit) numbers
    """
    if num < 20:
        last= nums[num-1]
    elif num < 1e2:
        right_result, left_result = split_num(num,1)
        last = get_tens(right_result, left_result)
    return last, right_result, left_result

def spell_3digit_num(num):
    """
    Main function that splits the digits and passes to individual bits of functions to do spell processing.
    This function only deals with 3 digit numbers.
    :param num: input number from teh user
    :return: Returns the spelling of a 3 digit number to caller
    """
    if num == 0:
        return 'zero'
        last, right_result, left_result = get20to100(num)
        return last
    elif num < 1e3:
        right_result, left_result_orig = split_num(num,2)
        if right_result == 0:
            return nums[left_result_orig-1] + " hundred"
        else:
            if right_result %10 == 0:
                last= tens[int(right_result/10)-1]
            else:
                num = right_result
                last, right_result, left_result = get20to100(num)
        return nums[left_result_orig-1]+" hundred and "+last

def get_tens(right_result, left_result):
    """
    This function returns the tens digit - whether its less than 20, or greater than 20 but less than 100
    :param right_result: input from right right part of the digit
    :param left_result: input from right left part of the digit
    :return: returns the spelling string of the 2-digit number
    """
    if right_result == 0:
        return tens[left_result-1]
    else:
        return tens[left_result-1]+" "+nums[right_result-1]

if __name__ == '__main__':
    main()

""" OUTPUT:
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hkw4 $ python3 main.py 0
zero
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hkw4 $ python3 main.py -1
negative one
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hkw4 $ python3 main.py -12
negative twelve
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hkw4 $ python3 main.py -123
negative one hundred and twenty three
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hkw4 $ python3 main.py 1234
one thousand two hundred and thirty four
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hkw4 $ python3 main.py 12345
twelve thousand three hundred and forty five
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hkw4 $ python3 main.py 123456
one hundred and twenty three thousand four hundred and fifty six
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hkw4 $ python3 main.py 1234567
one million two hundred and thirty four thousand five hundred and sixty seven
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hkw4 $ python3 main.py 1234568
one million two hundred and thirty four thousand five hundred and sixty eight
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hkw4 $ python3 main.py -12345689
negative twelve million three hundred and forty five thousand six hundred and eighty nine
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hkw4 $
"""
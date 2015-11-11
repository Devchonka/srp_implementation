"""
@author: Elena Menyaylenko
Homework #1.
Basic printing of an output.
"""
import datetime


def main():
    """main() is the main function for homework 1."""
    print("This is the first homework assignment and I wanted to learn to print dates.\n")

    today = datetime.date.today()
    print('Today is the {day}th in the month {month} of the year {year}!'.format(month=today.strftime('%B'),
                                                                                 day=str(today.day),
                                                                                 year=str(today.year)))


if __name__ == "__main__":
    main()


""" OUTPUT:
/usr/bin/python3.4 /home/elena/PycharmProjects/PythonCourse/Hwk/main.py
This is the first homework assignment and I wanted to learn to print dates.

Today is the 24th in the month September of the year 2015!

Process finished with exit code 0
"""
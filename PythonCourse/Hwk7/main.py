"""
Elena Menyaylenko
Hwk7 11/10/2015

Objectives:       Use inheritance
                 Practice iterative development

main.py file contains the test program and tester class for the Employee and Manager testing, as well as
the main program for running the script.
"""

from employee import Employee
import manager


class Employee_Tester(object):
    """
    A tester class containing several methods to test the Employee and Manager objects created.
    Creates a list of 5 people, the last 2 being managers.
    Allows to test the instance and the raise methods of this assignment.
    Contains  4 class variables that are just names used for testing the program.
    """
    employee_first_names = ['Abby', 'Lena', 'Jeremy', 'Sonia', 'Jerry']
    employee_last_names = ['Giles', 'Prolly', 'Jones', 'Smith', 'Kane']
    employee_ssns = [1234567, 23456789, 8787654, 8765836, 5372547]
    employee_salaries = [90500, 80700, 100000.99, 99000, 95000.50]

    def __init__(self):
        """
        Instantiation, allows for creation of None object in place of all_employees
        :return:None
        """
        self.all_employees = None
        print('Test class for employees is created.')

    def create_five_employees(self):
        """
        Allows for creation of 5 employee using the class variables defined for the test class.
        :return: Updates the all_employee variable to be a list of 5 employees (2 last ones managers)
        """
        if self.all_employees == None:
            self.all_employees = []
        for iteration, first, last, ssn, salary in zip(range(5), Employee_Tester.employee_first_names,
                                                       Employee_Tester.employee_last_names,
                                                       Employee_Tester.employee_ssns,
                                                       Employee_Tester.employee_salaries):
            if iteration > 2:  # the last 2 in list will be managers
                try:
                    new_employee = manager.Manager(first, last, ssn, salary, 'Sales Manager', 8.5)
                except TypeError:
                    print('Please note names must be strings, numbers must be ints or floats')
            else:
                try:
                    new_employee = Employee(first, last, ssn, salary)
                except TypeError:
                    print('Please note names must be strings, numbers must be ints or floats')
            self.all_employees.append(new_employee)

    def test_instance(self):
        """
        Tests which employees are just employees, and which are also managers
        :return: None, prints output of True/False for manager test to screen.
        """
        print('\n')
        for num, employee in enumerate(self.all_employees):
            print('is employee {} a manager? -{}'.format(num, isinstance(employee, manager.Manager)))
        print('\n')

    def test_raises(self):
        """
        Method prints the employee's earnings before AND after the percent raise.
        Percent raises are increased as the person in later in the list, with the last 2 managers
        getting the highest pay raise.
        :return: None, prints output of testing raises to screen.
        """
        print('\n')
        for employee_number, employee in enumerate(self.all_employees):
            print(employee)
            employee.giveRaise(employee_number*1.5+2)
            print(employee)
        print('\n')


def main():
    """
    Main function to create the test class and several instances of employees and managers and test them.
    """
    tester = Employee_Tester()
    tester.create_five_employees()

    tester.test_instance()
    tester.test_raises()

    # unsuccessful employee creations:
    print('Now to show robustness of class using exceptions:')
    try:
        wrong_employee = Employee(12345, 62352, 'sgfhdfh', 93704.93)
    except TypeError:
        print('Please note names must be strings, numbers must be ints or floats')

if __name__ == '__main__':
    main()

""" OUTPUT:
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hwk7 $ python3 main.py
Test class for employees is created.


is employee 0 a manager? -False
is employee 1 a manager? -False
is employee 2 a manager? -False
is employee 3 a manager? -True
is employee 4 a manager? -True




Giles, Abby : 1234567 : $90500.00
Employee received a 2.0 percent raise.
Giles, Abby : 1234567 : $92310.00
Prolly, Lena : 23456789 : $80700.00
Employee received a 3.5 percent raise.
Prolly, Lena : 23456789 : $83524.50
Jones, Jeremy : 8787654 : $100000.99
Employee received a 5.0 percent raise.
Jones, Jeremy : 8787654 : $105001.04
Smith, Sonia : 8765836 : $99000.00 Sales Manager 8.5
Employee received a 6.5 percent raise.
Smith, Sonia : 8765836 : $105435.00 Sales Manager 8.5
Kane, Jerry : 5372547 : $95000.50 Sales Manager 8.5
Employee received a 8.0 percent raise.
Kane, Jerry : 5372547 : $102600.54 Sales Manager 8.5


Now to show robustness of class using exceptions:
Please note names must be strings, numbers must be ints or floats
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hwk7 $

"""
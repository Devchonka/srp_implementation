"""
The employee.py file contains the Employee class which defines the object creation base (super)
class for employees.
"""

class Employee(object):
    def __init__(self, first_name, last_name, ssn, salary):
        """
        Instantiation of the class Employee.
        :param first_name: employee first name, must be string
        :param last_name: employee last name, must be string
        :param ssn: employee ssn, must be int
        :param salary: employee salary, must be in or float
        :return: an instance of the Employee class
        """
        self.first_name = first_name
        self.last_name = last_name
        if type(ssn) != int or not isinstance(salary, (int, float)):
            raise TypeError()
        self.ssn = int(ssn)
        self.salary = float(salary)

    def __str__(self):
        """
        Allows to print the instance directly.
        :return: a string specifying how to print an object of this type
        """
        return '{}, {} : {} : ${:.2f}'.format(self.last_name, self.first_name, str(self.ssn), self.salary)

    def giveRaise(self, percentRaise):
        """
        A method that allows to bumb up an employee's salary by the specified percentage.
        :param percentRaise: percent by which to increase employee salary
        :return: None, simply increase the self.salary in Employee object
        """
        if not isinstance(percentRaise, (float, int)):
            raise TypeError()
        self.salary += percentRaise / 100 * self.salary
        print('Employee received a {} percent raise.'.format(percentRaise))
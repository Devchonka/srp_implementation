"""
The manager.py class contains a subclass which inherits from the employee.Employee base class.
"""

import employee


class Manager(employee.Employee):
    """
    The Manager class inherits from Employee. It contains 2 additional variables (title, bonus)
    and its own __init__ and __str__ methods.
    The subclass can call all methods of the base class.
    """
    def __init__(self, first_name, last_name, ssn, salary, title, bonus):
        """
        Instantiation of the subclass Manager, inheriting from base super class Employee.
        :param first_name: employee first name, must be string
        :param last_name: employee last name, must be string
        :param ssn: employee ssn, must be int
        :param salary: employee salary, must be in or float
        :param title: manager title, must be string, only in subclass
        :param bonus: manager annual bonus, must be int, only in subclass
        :return: an instance of the Manager class
        """
        super().__init__(first_name, last_name, ssn, salary)
        if type(title) != str or not isinstance(bonus, (int, float)):
            raise TypeError()
        self.title = title
        self.bonus = bonus

    def __str__(self):
        """
        This method allows for the printing directly of the object.
        :return: returns a string of how an instance of this class is to be printed to the screen
        """
        return super().__str__() + ' {} {}'.format(self.title, self.bonus)
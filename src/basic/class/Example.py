# class ClassName:
#    'Optional class documentation string'
#    class_suite


class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @staticmethod
    def display_count():
        print "Total Employee %d" % Employee.empCount

    def display_employee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"
        Employee.empCount -= 1

# extra
Employee.display_count()

employee_one = Employee("Zara", 100000)
employee_one.display_employee()
Employee.display_employee(employee_one)

Employee.display_count()
employee_one.__del__()
Employee.display_count()

hasattr(employee_one, 'age')     # Returns true if 'age' attribute exists
setattr(employee_one, 'age', 8)  # Set attribute 'age' at 8
getattr(employee_one, 'age')     # Returns value of 'age' attribute
delattr(employee_one, 'age')     # Delete attribute 'age'

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

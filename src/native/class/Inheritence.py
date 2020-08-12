class Parent:  # define parent class
    parentAttr = 100

    def __init__(self):
        self.__secret = "secret message"
        print("Calling parent constructor")

    @staticmethod
    def parent_method():
        print('Calling parent method')

    @staticmethod
    def set_attr(attr):
        Parent.parentAttr = attr

    @staticmethod
    def get_attr():
        print("Parent attribute :", Parent.parentAttr)

    def print_secret_message(self):
        print(self.__secret)


class Child(Parent):  # define child class

    def __init__(self):
        super().__init__()
        print("Calling child constructor")

    @staticmethod
    def child_method():
        print('Calling child method')


print(Parent.parentAttr)
c = Child()  # instance of child
c.child_method()  # child calls its method
c.parent_method()  # calls parent's method
c.set_attr(200)  # again call parent's method
c.get_attr()  # again call parent's method
print(Parent.parentAttr)

c.print_secret_message()
c._Parent__secret = 327
c.print_secret_message()


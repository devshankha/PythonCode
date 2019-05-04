import abc
class Vehicle(abc.ABC):
    @abc.abstractmethod
    def display(self): pass

class Car(Vehicle):
    def display(self):
        print("This is a car")

a = Car()
a1 = Vehicle()
a.display()


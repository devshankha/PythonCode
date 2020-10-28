class Mammal(object):
    def __init__(self,name):
        print("%s is a warm blooded mammal "%(name))
        print("{} is a warm blooded mammal".format(name))

class Dog(Mammal):
    def __init__(self):
        print("Dog is an animal")
        super().__init__("dog")

d = Dog()


# good example of python class method
# Another way to look at this use of class methods is that they allow you to define alternative constructors for your
# classes. Python only allows one __init__ method per class. Using class methods it’s possible to add as many
# alternative constructors as necessary. This can make the interface for your classes self-documenting
# (to a certain degree) and simplify their usage.

#https://realpython.com/instance-class-and-static-methods-demystified/

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


s1 = Pizza.margherita()
s2 = Pizza.prosciutto()
#print(type(s1))


print(Pizza.prosciutto())



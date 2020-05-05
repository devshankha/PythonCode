
class A:
    def __init__(self):
        print('Initializing: class A')
class B(A):
    def __init__(self):

         super().__init__()
         print('Initializing: class B')
class C(B):
    def __init__(self):
         super().__init__()
         print('Initializing: class C')

x= C()



class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("In the constructor of Person "+self.name+" "+self.age)

class Teacher(Person):
    def __init__(self,name,age,address):
        self.address = address
        super().__init__(name,age)

c = Teacher("David","12","ECity")








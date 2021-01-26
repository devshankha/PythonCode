class Person:

    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        self.instance_method()

    def instance_method(self):
        print('success!')

personObj = Person()
'''
class class_name:
    def __new__(cls, *args, **kwargs):
        statements 
      
        

'''


# Python program to
# demonstrate __new__

# don't forget the object specified as base
class A(object):
    def __new__(cls):
        print("Creating instance")
        #return super(A, cls).__new__(cls)
        # In python 3 both the statements are similar
        return super().__new__(cls)

    def __init__(self):
        print("Init is called")

A()
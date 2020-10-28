class Foo(object):
    def __new__(cls,a):
        print("Creating Instance")
        #instance = super().__new__(cls)
        instance = super(Foo, cls).__new__(cls)
        #even this line can be used
        #instance = object.__new__(cls)
        return instance

    def __init__(self,a):
        print("In init")
        self.a = a

    def bar(self):
        pass
a = Foo(7)






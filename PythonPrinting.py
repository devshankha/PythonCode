class Test:
    '''
    In Python, this can be achieved by using __repr__ or __str__ methods. __repr__
    is used if we need a detailed information for debugging while __str__ is used
    to print a string version for the users.

    Python uses __repr__ method if there is no __str__ method

    If no __repr__ method is defined then the default is used.

    examining an object through interpreter always calls repr

    '''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        #return "From repr method Test a:% s b:% s" % (self.a, self.b)
        return "REPR The value of a is {} and b is {}".format(self.a,self.b)

    def __str__(self):
        return "The value of a is {} and b is {}".format(self.a, self.b)

        # Driver Code
t = Test(1234, 5678)
# This calls __str__()
print(t)
# This calls __repr__()
print([t])
print("-----------------")
print(str(t))
print(repr(t))

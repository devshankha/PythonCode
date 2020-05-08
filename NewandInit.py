
# Usage of new operator
class A1(object):
    def __init__(self):
        print("In initializing")
        self.name="David"

    def __new__(cls, *args, **kwargs):
        print("In the creation")
        print(cls)
        print(args)
        print(kwargs)
        return super(A1,cls).__new__(cls)


x = A1()
print(x.name)

# control the number of instances

class Point:
    __noOfInstances=0
    MAX = 3
    def __new__(cls, *args, **kwargs):
        if (Point.__noOfInstances > 3):
            raise Exception("Cannot create more than 3")
        Point.__noOfInstances = Point.__noOfInstances+1
        return super().__new__(cls)

x1 = Point()
x1 = Point()
x1 = Point()
x1 = Point()

class Check:
    def __new__(cls):
        return 3

print(type(Check()))




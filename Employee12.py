class Employee:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def printEmployee(self):
         print("Name is ",self.name,end='')
         print(", Age is ",self.age,end='')
         print(", City is ",self.city)
         print("Name is {} and city is {}".format(self.name,self.city))

e = Employee("David",12,"California")
e.printEmployee()


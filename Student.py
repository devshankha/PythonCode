class Student:
 a = 67	
 def __init__(self):
   self.name = "David"
   self.age = 20
   self.marks = 96
 def talk(self):
   print("My name is",self.name)
   print("My age is",self.age)
   print(" My marks are ",self.marks)
   #print("How are you",a)
s = Student()
s.talk()

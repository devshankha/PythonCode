class Emp:
 def __init__(self,name):
   self.name = name
   print ("In the constructor")

 def displayName(self):
   print (self.name)
t = Emp("David")
t.displayName()


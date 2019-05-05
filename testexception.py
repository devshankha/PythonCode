a = [1,2,3]
s1 = "David"

try:
    #print("First element is %d",%a[0])
    print("Second element = %d"  %(a[1]))
    print("Second element is %s" %s1)
    print("Fourth element is %d", a[4])
except IndexError:
    print("Index error occured")

finally:
    print("Will always come here")

class Person :
    def __init__(self,name,age=54):
         self.name = name
         self.age = age

    def display(self):
         print("Name is %s" %self.name )
         print("Age is %d" % self.age)

k = Person("Hussain")
k.display()


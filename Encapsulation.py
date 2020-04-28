class Robot(object):
   def __init__(self):
      self.a = 123
      self._b = 123
      self.__c = 123

obj = Robot()
print(obj.a)
print(obj._b)
#print(obj.__c)


class Person:
    def __init__(self):
        self.name = 'Manjula'
        self.__lastname = 'Dube'

    def PrintName(self):
        return self.name + ' ' + self.__lastname


# Outside class
P = Person()
print(P.name)
print(P.PrintName())
# print(P.__lastname)
print(P._Person__lastname)

class AB:
    def main(self):
        self.a = 5
        self._b = 6
        self.__c = 7

cv = AB()
print(cv.a)
print(cv._b)
print(cv._AB__c)






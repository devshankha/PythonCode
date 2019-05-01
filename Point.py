class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      check = self.__class__.__module__
      print (class_name, "destroyed")
      print (check)

pt1 = Point()
del pt1

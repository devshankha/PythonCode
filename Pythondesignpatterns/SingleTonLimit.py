#Limit the number of instances
class Singleton(object):
    _instance = None  # Keep instance reference

    def __new__(cls, *args, **kwargs):
        #if  cls._instance == None:
        if not cls._instance:
            #cls._instance = object.__new__(cls, *args, **kwargs)
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

c1 = Singleton()
c2 = Singleton()
c3 = Singleton()
print(c1 == c3)
print(c2 == c3)


class LimitedInstances(object):
    _instances = []  # Keep track of instance reference
    limit = 5

    def __new__(cls, *args, **kwargs):
        if not len(cls._instances) <= cls.limit:
            raise RuntimeError("Count not create instance. Limit %s reached" % cls.limit)
        instance = object.__new__(cls, *args, **kwargs)
        cls._instances.append(instance)
        return instance

    def __del__(self):
        # Remove instance from _instances
        self._instance.remove(self)






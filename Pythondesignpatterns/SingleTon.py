class Singleton:
    __instance = None

    @staticmethod    
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Cannot create more than one instance")
        else:
            Singleton.__instance = self


c2 = Singleton()
c3 = Singleton.getInstance()
c4 = Singleton.getInstance()
#print(c1)
print(c2)
print(c3)
print(c4)




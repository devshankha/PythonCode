class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass

rm1 = Borg()
rm2 = Borg()
print(rm1)
print(rm2)
rm1.state = 'Idle'
rm2.state = 'Running'
print(rm1)
print(rm2)
rm2.state = 'Zombie'
print(rm1)
print(rm2)

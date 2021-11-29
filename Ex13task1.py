import random


class Car:
    def __init__(self, owner_name, code):
        self.o_name = owner_name
        self.code = code
        self.__key = self._ke()

    def _ke(self):
        "Данные машины"
        self.__code = "0123{}open".format(self.o_name)
        digits = "0123456789"
        alp = "qwertyuiopasdfghjklzxcvbnm"
        al = digits + alp
        password = ""
        for _ in range(10):
            password += random.choice(al)
        return password

    def unlock(self, k):
        "Код с ключа машины"
        if k == self.__key:
            return "The car is open"
        else:
            return "It's wrong key"

    def getKey(self):
        if self.code == self.__code:
            kk = self.__key
            return kk
        else:
            return "Leave this car"

    def setCode(self, cod):
        self.code = cod
        return self.getKey()


mark = Car("Max", "123dfqwe")
print(mark.unlock("1234gbbh"))
print(mark.getKey())
print(mark.setCode("0123Maxopen"))
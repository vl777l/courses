from random import randrange


class Transport:
    def __init__(self, name="Mark", speed=50, fuel="patrol"):
        self.speed = speed
        self.fuel = fuel
        self.name = name


class Terrestrial(Transport):
    weightperson = 75

    def __init__(self, name, countofseats=2):
        super().__init__(name)
        self.cofseats = countofseats

    def weightpeople(self):
        weight = self.cofseats*randrange(20, self.weightperson)
        return weight


class Car(Terrestrial):
    def pepe(self):
        if "coup" in self.name:
            self.cofseats = self.cofseats
            print(super().weightpeople())
        else:
            self.cofseats = 5
            print(super().weightpeople())


class Railway(Terrestrial):
    def __init__(self, name, countofwagons=3):
        super().__init__(name)
        self.fuel = "coal"
        self.cofwagons = countofwagons

    def peop(self):
        if "sv" in self.name:
            self.cofseats = 14
        elif "coup" in self.name:
            self.cofseats = 28
        else:
            self.cofseats = 42
        print(super().weightpeople() * self.cofwagons)


class Water(Transport):
    speedair = 10

    def __init__(self, name, countofseats=4):
        super().__init__(name)
        self.cofseats = countofseats

    def speeddepends(self):
        if "air pas" in self.name:
            self.speed += self.speedair
            return self.speed
        elif "head" in self.name:
            self.speed -= self.speedair
            return self.speed
        else:
            return self.speed


class WaterBike(Water):
    def danger(self):
        if self.speeddepends() >=55:
            return "DANGEROUS! You can`t go alone!"
        else:
            return "Have a good day!"


dodg = Car("dodg chalanger coupe")
dodg.pepe()

tran = Railway("Vip")
tran.peop()

bibi = WaterBike("Spar air pas")
print(bibi.danger())
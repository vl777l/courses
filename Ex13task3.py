class Temperature:
    def __init__(self, temperature=0):
        self.temp = temperature


class Transform(Temperature):
    def to_celcium(self):
        if "C" in scale:
            return self.temp
        else:
            return (self.temp - 32) * 5/9

    def to_fahrenheit(self):
        if "F" in scale:
            return self.temp
        else:
            return (self.temp * 1.8) + 32

    @property
    def temp(self):
        print("Getting value...")
        return self._temp

    @temp.setter
    def temp(self, value):
        print("Setting value...")
        global scale
        scale = input("Indicate scale (F or C): ")
        if "F" in scale:
            if value < -459.67:
                raise ValueError("Temperature below 459 is not possible")
            self._temp = value
        elif "C" in scale:
            if value < -273.15:
                raise ValueError("Temperature below -273 is not possible")
            self._temp = value
        else:
            raise ValueError("You didn`t indicate scale")


human = Transform(37)

print(human.temp)

print(human.to_fahrenheit())

coldest_thing = Transform(-300)
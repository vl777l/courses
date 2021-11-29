class Car:
    def __init__(self, name, year, engine, fuel, equipment):
        self.name = name
        self.year = year
        self.engine = engine
        self.fuel = fuel
        self.equipment = equipment

    def __str__(self):
        return f"Марка авто {self.name}\nГод выпуска {self.year}\nОбъём двигателя {self.engine}\nТопливо{self.fuel}\n" \
               f"Комплектация {self.equipment} "


def menu():
    return print("Если вы хотите приобрести автомобиль марки:\nBMW введите 1\nAudi введите 2\nNissan введите 3\n"
                 "Porsche введите 4\nLexus введите 5\nПокинуть автосалон 0")


class AutoShowroom:
    carlist = ["bmw", "audi", "nissan", "porsche", "lexus"]
    print(carlist)
    menu()
    def sale_car(self, n):
        while n != 0:
            if n == 1:
                return print(Car("bmw", 2020, 2.0, "бензин", "М"))
            elif n == 2:
                return print(Car("audi", 2021, 2.5, "дизель", "rs6"))
            elif n == 3:
                return print(Car("nissan", 2018, 2.5, "газ/бензин", "Rogue SL"))
            elif n == 4:
                return print(Car("porsche", 2020, 3.0, "бензин", "911"))
            elif n == 5:
                return print(Car("lexus", 2016, 3.5, "бензин", "ls 570"))
            elif n == 0:
                return print("Bye!")
            else:
                menu()
                n = int(input("Сделайте выбор: "))


n = int(input("Сделайте выбор: "))
AutoShowroom().sale_car(n)
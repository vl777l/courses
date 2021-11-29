class Book:
    "Information about book"
    def __init__(self, author, name, year, publication, genre):
        self.author = author
        self.name = name
        self.year = year
        self.publication = publication
        self.genre = genre

    def __str__(self):
        return f"Автор {self.author},\nназвание {self.name},\nгод печати {self.year},\n" \
               f"издательсво {self.publication},\nжанр {self.genre}"

    def __eq__(self, other):
        return self.author == other.author and self.name == other.name and self.year == other.year \
                and self.publication == other.publication and self.genre == other.genre

    def __ne__(self, other):
        return self.author != other.author and self.name != other.name and self.year != other.year \
               and self.publication != other.publication and self.genre != other.genre

    def __repr__(self):
        return f"Автор книги {self.author},\nназвание {self.name},\nгод выпуска {self.year},\n" \
               f"издательсво {self.publication},\nжанр {self.genre}"


book1 = Book("Джон Дуглас", "Охотник за разумом", 2016, "Рипол классик", "кириминал")
book2 = Book("Луиза Мэй", "Маленькие женщины", 2017, "Азбука", "роман")
book3 = Book("Михаил Лабковский", "Хочу и буду", 2020, "Бук шеф", "психология")

book = [book1, book2, book3]

for b in range(len(book)):
    if b != len(book)-1:
        print(book[b].__eq__(book[b+1]))
    else:
        print(book[b].__eq__(book[0]))

for bo in range(len(book)):
    if bo != len(book)-1:
        print(book[bo].__ne__(book[bo+1]))
    else:
        print(book[bo].__ne__(book[0]))

for boo in range(len(book)):
    print(book[boo])
    print("\n")
    print(book[boo].__repr__())
    print("\n")
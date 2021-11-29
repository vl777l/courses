class Book:
    """Information about book"""
    def __init__(self, author, name, year, publication, genre, list_reviews):
        self.author = author
        self.name = name
        self.year = year
        self.publication = publication
        self.genre = genre
        self.list_reviews = list_reviews

    def __str__(self):
        return f"Автор {self.author},\nназвание {self.name},\nгод печати {self.year},\n" \
               f"издательсво {self.publication},\nжанр {self.genre},\n{self.list_reviews}"


class Reviews:
    """Book reviews"""
    def __init__(self, user, book, comment):
        self.user = user
        self.book = book
        self.comment = comment

    def __str__(self):
        return f"{self.user} writes about book {self.book}: {self.comment}"


user1 = str(input("Укажите ваше имя: "))
book1_review = str(input("Напишите отзыв о книге 'Охотник за разумом': "))
book2_review = str(input("Напишите отзыв о книге 'Маленькие женщины': "))
book3_review = str(input("Напишите отзыв о книге 'Хочу и буду': "))


book1 = Book("Джон Дуглас", "Охотник за разумом", 2016, "Рипол классик", "кириминал",
             Reviews(user1, "Охотник за разумом", book1_review))
book2 = Book("Луиза Мэй", "Маленькие женщины", 2017, "Азбука", "роман",
             Reviews(user1, "Маленькие женщины", book2_review))
book3 = Book("Михаил Лабковский", "Хочу и буду", 2020, "Бук шеф", "психология",
             Reviews(user1, "Хочу и буду", book3_review))
print(book1)
print("\n")
print(book2)
print("\n")
print(book3)
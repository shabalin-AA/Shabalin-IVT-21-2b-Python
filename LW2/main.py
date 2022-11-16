import datetime



class Printing:
    def __init__(self, name: str, year: int):
        self.__name = name
        self.__year = year


    def print(self):
        print("Name:", self.__name)
        print("Year:", self.__year)



class Magazine(Printing):
    def __init__(self, name: str, year: int, date: datetime):
        super().__init__(name, year)
        self.__date = date


    def print(self):
        super().print()
        print("Date:", self.__date)



class Book(Printing):
    def __init__(self, name: str, year: int, genre: str):
        super().__init__(name, year)
        self.__genre = genre


    def print(self):
        super().print()
        print("Genre:", self.__genre)



class Schoolbook(Book):
    def __init__(self, name: str, year: int, subject: str):
        super().__init__(name, year, "Science")
        self.__subject = subject


    def print(self):
        super().print()
        print("Subject:", self.__subject)



p = Magazine("Cooking", 1990, datetime.datetime(1990, 5, 17))
p.print()

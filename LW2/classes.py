import datetime
import json



class Printing:
    def __init__(self):
        self.__name = "name"
        self.__year = 1


    def print(self):
        print("Name:", self.__name)
        print("Year:", self.__year)


    def json_load(self, json_filepath: str):
        with open(json_filepath) as f:
            obj = json.load(f)
            self.__name = obj["name"]
            self.__year = obj["year"]


    def json_save(self, json_filepath: str):
        to_json = {
            "name": self.__name,
            "year": self.__year
        }
        with open(json_filepath, 'w') as f:
            json.dump(to_json, f)



class Magazine(Printing):
    def __init__(self):
        super().__init__()
        self.__date = datetime.datetime(2000, 1, 1)


    def print(self):
        super().print()
        print("Date:", self.__date)


    def json_load(self, json_filepath: str):
        with open(json_filepath) as f:
            obj = json.load(f)
            self.__name = obj["name"]
            self.__year = obj["year"]
            self.__date = datetime.datetime(
                obj["date"]["year"],
                obj["date"]["month"],
                obj["date"]["day"]
            )


    def json_save(self, json_filepath: str):
        to_json = {
            "name": self.__name,
            "year": self.__year,
            "date": {
                "year":  self.__date.year,
                "month": self.__date.month,
                "day":   self.__date.day
            }
        }
        with open(json_filepath, 'w') as f:
            json.dump(to_json, f)



class Book(Printing):
    def __init__(self):
        super().__init__()
        self.__genre = "genre"


    def print(self):
        super().print()
        print("Genre:", self.__genre)


    def json_load(self, json_filepath: str):
        with open(json_filepath) as f:
            obj = json.load(f)
            self.__name = obj["name"]
            self.__year = obj["year"]
            self.__genre = obj["genre"]


    def json_save(self, json_filepath: str):
        to_json = {
            "name": self.__name,
            "year": self.__year,
            "genre": self.__genre
        }
        with open(json_filepath, 'w') as f:
            json.dump(to_json, f)



class Schoolbook(Book):
    def __init__(self):
        super().__init__()
        self.__subject = "subject"


    def print(self):
        super().print()
        print("Subject:", self.__subject)


    def json_load(self, json_filepath: str):
        with open(json_filepath) as f:
            obj = json.load(f)
            self.__name = obj["name"]
            self.__year = obj["year"]
            self.__genre = obj["genre"]
            self.__subject = obj["subject"]


    def json_save(self, json_filepath: str):
        to_json = {
            "name": self.__name,
            "year": self.__year,
            "genre": self.__genre,
            "subject": self.__subject
        }
        with open(json_filepath, 'w') as f:
            json.dump(to_json, f)

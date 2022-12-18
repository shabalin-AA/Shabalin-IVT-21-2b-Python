from datetime import datetime
import json



class Printing:
    def __init__(self, name):
        self.__name = name
        self.__year = datetime.now().year


    @property
    def name(self):
        return self.__name


    @property
    def year(self):
        return self.__year


    def __repr__(self):
        return "Printing " + repr(self.__name) + " " + str(self.__year)


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
    def __init__(self, name):
        super().__init__(name)
        self.__date = datetime.now()


    @property
    def date(self):
        return self.__date


    @property
    def name(self):
        return super().name


    def __repr__(self):
        return "Magazine " + repr(super().name) + " " + str(self.__date.day) + "." + str(self.__date.month) + "." + str(self.__date.year)


    def json_load(self, json_filepath: str):
        with open(json_filepath) as f:
            obj = json.load(f)
            self.__name = obj["name"]
            self.__year = obj["year"]
            self.__date = datetime(
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

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import re

def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


def reduce(list, acc, fn):
    for el in list:
        acc = fn(el, acc)
    return acc


def map(list, fn):
    for i in range(len(list)):
        list[i] = fn(list[i])
    return list


# from handle init data
l = [1, 2, 3, 4, 5]
print(map(l, lambda x: x ** 2))


# from dataset
titanic = pd.read_csv('titanic.csv', header = 0, delimiter = ',')[:20]

titanic_male_survived = titanic[(titanic.Sex == 'male') & (titanic.Survived == 1) & (titanic.Age > 0)]

average_age = reduce(titanic_male_survived['Age'], 0, lambda x, acc: x + acc) / len(titanic_male_survived['Age'])

print(average_age)


# from parsed data
url = 'https://tophit.ru/ru/chart/russia_allmedia/weekly/current/all/all'
req = requests.get(url)
soup = bs(req.text, "html.parser")
chart = soup.find_all("tr", class_ = 'b-chart-item green2')

tracks =[]
for track in chart:
    name = track.find('a', class_='black').text
    radio = track.find('td', class_='bigint').text
    tracks.append([name, radio.replace(' ', '')])


print(reduce(tracks, 0, lambda track, acc: acc + int(track[1]) if has_cyrillic(track[0]) else acc))

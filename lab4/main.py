from bs4 import BeautifulSoup
import requests


def reduce(list, acc, fn):
    for el in list:
        acc = fn(el, acc)
    return acc


def map(list, fn):
    for i in range(len(list)):
        list[i] = fn(list[i])
    return list


l = [1, 2, 3, 4, 5]

def f(x, acc):
    return acc * x

def f2(x):
    return x + 5


#print(reduce(l, 1, lambda x, acc: x * acc))
#print(map(l, lambda x: x + 5))


url = 'https://zenrows.com'
page = requests.get(url)

filtered_news = []
all_news = []

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.title.string)

#https://khashtamov.com/ru/pandas-introduction/

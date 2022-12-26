import pandas as pd


def reduce(list, acc, fn):
    for el in list:
        acc = fn(el, acc)
    return acc


def map(list, fn):
    for i in range(len(list)):
        list[i] = fn(list[i])
    return list


l = [1, 2, 3, 4, 5]

#print(reduce(l, 1, lambda x, acc: x * acc))
#print(map(l, lambda x: x + 5))


titanic = pd.read_csv('titanic.csv', header = 0, delimiter = ',',
    names = ["PassengerID","Name","PClass","Age","Sex","Survived","SexCode"])[:20]

titanic_male_survived = titanic[(titanic.Sex == 'male') & (titanic.Survived == 1)]

print(titanic_male_survived)

average_age = reduce(titanic_male_survived['Age'], 0, lambda x, acc: x + acc if x > 0 else acc) / len(titanic_male_survived['Age'])

print(average_age)

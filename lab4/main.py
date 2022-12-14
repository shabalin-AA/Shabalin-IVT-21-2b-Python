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


print(reduce(l, 1, f))
print(map(l, f2))

def func1():
    pass



def func2():
    pass


def calculator(number_list: list, koef: int):
    tmp = []
    for i in number_list:
        tmp.append(i * koef)
    sum = 0
    for i in tmp:
        sum = sum + i
    return sum
r = calculator([1,2,3,4],2)
print(r)
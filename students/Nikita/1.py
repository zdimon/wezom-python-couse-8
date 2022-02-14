def func1():
    pass



def func2():
    pass


def calculator(number_list: list,koef: int):
    print(number_list)
    tmp = []
    for number in number_list:
        tmp.append(number*koef)
    print(tmp)
    
numb = calculator([1,2,3,4],2)

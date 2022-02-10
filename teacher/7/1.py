def func1():
    pass



def func2():
    pass


def calculator(number_list: list,koef: int):
    print(number_list)
    tmp = []
    for number in number_list:
        print(number*koef)

calculator([1,2,3,4],2) 

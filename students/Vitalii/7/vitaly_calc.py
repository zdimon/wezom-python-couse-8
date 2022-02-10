def calc(spisok: list,koef: int):
    print(spisok)
    tmp = []
    for number in spisok:
        sum = number*koef

        tmp.append(sum)
    print(tmp)

    res = 0
    for num in tmp:
        res= num + res

    print (res)

calc([3,2,5,4,],5)    


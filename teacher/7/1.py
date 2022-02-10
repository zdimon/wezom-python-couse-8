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

calculator([1,2,3,4],2) 

def calc(spisok: list,koef: int):
    tmp = []
    for number in spisok:
        tmp.append(number*koef)
    res = 0
    for num in tmp:
        res = num + res
    return res

d = calc([1,2,3,4],2) 
print(d)

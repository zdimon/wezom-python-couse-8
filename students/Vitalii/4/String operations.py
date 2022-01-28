stroka = ('one-two-tree-for')
print (stroka)
# разделяем на список
res =  stroka.split("-")
# получаем кол=во в списке
namber_list = len(res)
#print (namber_list)
i = 0                  
temp2 = ""  
while i < namber_list:
    n = i+1
    temp = str(n) + "." + res[i] + "-"
    i += 1
    temp2 = temp2 + temp

#вывод
print(temp2[:-1])
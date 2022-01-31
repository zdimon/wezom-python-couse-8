str1 = 'one-two-tree-for'
list1 = str1.split('-')
print(list1)

for i in range(1,5,1) :
    stroka1 = str(i)+ '.' + list1[i - 1] + '-'
    stroka = stroka + stroka1
    print(stroka)
print(stroka)
    
    
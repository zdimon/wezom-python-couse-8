stroka = '2+5+7+12'
list_s = stroka.split('+')
print(list_s)
i = 0
sum = 0
while i < len(list_s):
    sum = sum + int(list_s[i])
    i +=1
print (sum)
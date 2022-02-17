
'''
213.139.210.147
root
VFB9J%eg

webmaster
123

'''

def calc(*args, **kwargs):
    result = 0
    print(kwargs)
    if kwargs["operation"] == '+':
        for number in args:
            result = result + number
    if kwargs["operation"] == '-':
        for number in args:
            result = result - number
    return result

r = calc(300,5,4,5,6,7,operation='+', format='double')

def wrapper(func):
    def inside():
        return '<h1>%s %s</h1>' % (func(),4)
    return inside

@wrapper
def say_hello():
    return "Hello"



print(say_hello())






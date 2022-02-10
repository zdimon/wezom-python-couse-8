import random
from .lib import create_deck
' цикл по масти'
deck = create_deck()
hend = deck[0:2]
accaunt=  0

for card in hend:
    print(card)
    tmp = card.split('-')
    print(tmp[0])
    accaunt = accaunt + int(tmp[0])
print(accaunt)
if accaunt>21:
    print('проиграл')
else:
    print('выйграл')
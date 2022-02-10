print('Start game')
from lib.library import create_deck

deck = create_deck()
hand = deck[0:4]
account = 0
for card in hand:
    print(card)
    tmp = card.split('-')
    print(tmp[0])
    account = account + int(tmp[0])

print(account)

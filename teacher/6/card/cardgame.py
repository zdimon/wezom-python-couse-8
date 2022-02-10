print('Start game')
from lib.library import create_deck, count_points

deck = create_deck()
hand = deck[0:4]
account = count_points(hand)
print(account)

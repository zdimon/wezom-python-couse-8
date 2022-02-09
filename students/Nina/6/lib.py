import random


input random
def create_deck():
    faces =['diamond','club','heart','spade']
cards =['6','7','8','9','10']

deck = create_deck()

for face in faces:
    for card in cards:
        print(card+'-'+face)
        deck.append(card+'-'+face)
print (deck)
random.shuffle(deck)







    return deck
import random
'''
на нужно получить список карт
fases = ['diamond', 'club', 'heart', 'spade']
cards = ['2','6','7'....]
deck = ['diamond-6','club-q','heart-a','spade-k', 'spade-j']
deck = []
for face in fases:
    print(face)
    for card in cards:
        print(card)
        deck.append(card) 
print(deck)
'''
print('Start game')
faces = ['diamond', 'club', 'heart', 'spade']
cards = ['6','7','8']
deck = []
for face in faces:
    for card in cards:
        print(card+'-'+face)
        deck.append(card+'-'+face)


print(deck)
random.shuffle(deck)
print(deck)

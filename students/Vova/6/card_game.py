import random
print('Start game')
faces = ['diamond', 'club', 'heart', 'spade']
cards = ['2','3','4','5','6','7','8','9','10']
deck = []
for face in faces:
    for card in cards:
        #print(card+'-'+face)
        deck.append(card+'-'+face)
#print(deck)
random.shuffle(deck)
hand = deck[0:4]
account = 0
for card in hand:
    print(card)
    tmp = card.split('-')
    print(tmp[0])
    account = account + int(tmp[0])
if account > 21:
    print('Lose')
elif account == 21:
    print('win')
else:
    print('try again')
print(account)
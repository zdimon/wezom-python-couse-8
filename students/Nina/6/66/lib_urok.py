import random

def create_deck():
    faces = ['diamond', 'club', 'heart', 'spade']
    cards = ['2','3','4','5','6','7','8','9']
    deck = []
    for face in faces:
        for card in cards:
            deck.append(card+'-'+face)
    random.shuffle(deck)
    return deck 
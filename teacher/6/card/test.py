from lib.library import create_deck

deck = create_deck()
if len(deck) != 32:
    print('Test failed!!!')
    print(f'this {len(deck)} is not equal {32}')
else:
    print('OK')
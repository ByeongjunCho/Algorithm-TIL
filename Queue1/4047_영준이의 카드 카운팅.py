

T = int(input())

for tc in range(1, T+1):
    card_deck = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    card = input()
    split_card = []
    for i in range(0, len(card), 3):
        split_card.append(card[i:i+3])

    if len(split_card) != len(set(split_card)):
        print('#{} {}'.format(tc, 'ERROR'))
    else:
        for k in split_card:
            card_deck[k[0]] -= 1
        print('#{} {} {} {} {}'.format(tc, card_deck['S'], card_deck['D'], card_deck['H'], card_deck['C']))



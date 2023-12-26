import collections

# part1
hands = []
with open('../../test/2023/2023_day7') as f:
    contents = f.readlines()
    for element in contents:
        element = element.split()
        cards, bid = element[0], int(element[1])

        numeric_value_of_cards = ['23456789TJQKA'.index(i) for i in cards]
        card_count = collections.Counter(cards)
        card_count_sorted = tuple(sorted(card_count.values()))

        type = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)].index(card_count_sorted)

        hands.append(((type, *numeric_value_of_cards), bid))

sorted_hands = sorted(hands)

total = 0
for i, (_, bid) in enumerate(sorted_hands):
    total += (i + 1) * bid
print(total)

hands_2 = []
# part2
with open('../../test/2023/2023_day7') as f:
    contents = f.readlines()
    for element in contents:
        element = element.split()
        cards, bid = element[0], int(element[1])
        numeric_value_of_cards = ['J23456789TQKA'.index(i) for i in cards]
        types = []
        for card in 'J23456789TQKA':
            card_count = collections.Counter(cards.replace('J', card))
            card_count_sorted = tuple(sorted(card_count.values()))
            type = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)].index(card_count_sorted)
            types.append(type)
        hands_2.append(((max(types), *numeric_value_of_cards), bid))

sorted_hands_2 = sorted(hands_2)

total_2 = 0
for i, (_, bid) in enumerate(sorted_hands_2):
    total_2 += (i + 1) * bid
print(total_2)

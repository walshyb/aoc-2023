from collections import defaultdict
from functools import cmp_to_key

# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'K': 12,
    'Q': 13,
    'A': 14,
}

# Types:
# Five of a Kind: 7 points
# Four of a Kind: 6 points
# Full House: 5 points
# Three of a Kind: 4 points
# Two Pair: 3 points
# One Pair: 2 points
# High Card: 1 point

# (hand_value, type, bid)
hands = []


# returns a reverse-frequency chart
def count_cards(hand):
    frequencies = defaultdict(int)
    for char in hand:
        frequencies[char] += 1

    reverse = defaultdict(list)
    for key in frequencies:
        occurrences = frequencies[key]
        reverse[occurrences].append(key)

    return reverse


def get_type(hand):
    # 5 of a kind
    if len(set(hand)) == 1:
        return 7

    # Four of a kind or full house
    if len(set(hand)) == 2:
        first_item = hand[0]

        # Four of a kind
        if hand.count(first_item) == 1 or hand.count(first_item) == 4:
            return 6
        else:
            # Full house
            return 5

    # High card
    if len(set(hand)) == 5:
        return 1

    occurrences = count_cards(hand)

    # Three of a kind
    if occurrences[3]:
        return 4

    # Two Pair
    if len(occurrences[2]) == 2:
        return 3

    if len(occurrences[2]) == 1:
        return 2

    # Shouldn't get here
    return 0


def compare(hand1_tuple, hand2_tuple):
    hand1 = hand1_tuple[0]
    hand2 = hand2_tuple[0]

    type1 = get_type(hand1)
    type2 = get_type(hand2)

    if type1 - type2 > 0:
        return 1
    elif type1 - type2 < 0:
        return -1

    # They're equal

    for i in range(len(hand1)):
        c1 = values[hand1[i]]
        c2 = values[hand2[i]]

        if c1 - c2 > 0:
            return 1
        elif c1 - c2 < 0:
            return -1

    # Shouldn't get here?
    return 0


hands = []

for line in lines:
    [hand, bid] = line.split(' ')
    bid = int(bid.strip())

    hands.append((hand, bid))

hands.sort(key=cmp_to_key(compare))

result = 0
for index, tup in enumerate(hands):
    bid = tup[1]
    result += (index + 1) * bid

print(result)

# 253673509 too high

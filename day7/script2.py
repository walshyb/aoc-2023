from collections import defaultdict
from functools import cmp_to_key

# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

values = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 11,
    'K': 12,
    'A': 13,
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

# Really get most common
def get_highest(hand):
    hand = hand.replace('J', '')
    if hand == '':
        return 'J'

    freqs = defaultdict(list)

    for c in hand:
        count = hand.count(c)
        freqs[count].append(c)

    highest_card = None
    for i in range(len(hand),0, -1):
        if len(freqs[i]) == 1:
            print(hand, freqs[i][0])
            return freqs[i][0]
        elif len(freqs[i]) > 1:
            cards = freqs[i]
            highest = cards[0]

            for card in cards:
                if values[card] > values[highest]:
                    highest = card

            print(hand, highest)
            return highest



    print(hand, highest_card)
    return highest_card


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
    print('comp', hand1_tuple[0], hand2_tuple[0])
    hand1_original = hand1_tuple[0]  # JKKK2
    hand1_new = None                 # KKKK2
    if 'J' in hand1_original:
        highest = get_highest(hand1_original)
        hand1_new = hand1_original.replace('J', highest)
        type1 = get_type(hand1_new)
    else:
        type1 = get_type(hand1_original)

    hand2_original = hand2_tuple[0]  # QQQQ2
    hand2_new = None                 # None
    if 'J' in hand2_original:
        highest = get_highest(hand2_original)
        hand2_new = hand2_original.replace('J', highest)
        type2 = get_type(hand2_new)
    else:
        type2 = get_type(hand2_original)

    if type1 - type2 > 0:
        #print(hand1_new or hand1_original, hand2_new or hand2_original, 1)
        return 1
    elif type1 - type2 < 0:
        #print(hand1_new or hand1_original, hand2_new or hand2_original, -1)
        return -1


    # They're equal

    for i in range(len(hand1_original)):
        c1 = values[hand1_original[i]]
        c2 = values[hand2_original[i]]

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
    result += ((index + 1) * bid)
    #print(tup[0], tup[0].replace('J', get_highest(tup[0])),index +1, bid, result)

print(result)

# Too high 253525067
# too high 253335546
# 253996296 high
# 253253225 right


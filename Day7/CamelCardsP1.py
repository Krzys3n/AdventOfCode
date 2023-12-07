
card_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,  # Walet
    'Q': 12,  # Dama
    'K': 13,  # Król
    'A': 14,  # As
}

hand_type_values= {
    'Five' : 7,
    'Four' : 6,
    'Fullhouse' : 5,
    'Three' : 4,
    'TwoPair' : 3,
    'OnePair' : 2,
    'HighCard' : 1

}
def get_hand_value(hand):
    return [card_values[card] for card in hand]
def hand_type(hand):
    hand_type = "HighCard"
    card_hand_count = {
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        'T': 0,
        'J': 0,  # Walet
        'Q': 0,  # Dama
        'K': 0,  # Król
        'A': 0,  # As}
    }
    for card in hand:
        card_hand_count[card] += 1
    print(list(filter(lambda x: x > 0, card_hand_count.values())))
    twos = 0
    for x in card_hand_count.values():
        if x == 2:
            twos += 1
    if twos == 2:
        hand_type = 'TwoPair'
    if twos == 1:
        hand_type = 'OnePair'
    if any((x==5) for x in card_hand_count.values()):
        hand_type = 'Five'
    if any((x==4) for x in card_hand_count.values()):
        hand_type = 'Four'
    if any((x==3 ) for x in card_hand_count.values()):
        if any((x == 2) for x in card_hand_count.values()):
            hand_type = 'Fullhouse'
        else:
            hand_type = 'Three'

    return hand_type


with open("input.txt") as file:
    hands_ordered = [[],[],[],[],[],[],[]]
    hand_bid_dict = {}
    for line in file:
        hand = line.split(" ")[0]
        bid = line.split(" ")[-1]
        bid = bid.split('\n')[0]
        print(hand_type(hand))
        hands_ordered[hand_type_values[hand_type(hand)]-1].append(hand)
        hand_bid_dict[hand] = bid

for i in range(0,7):
    hands_ordered[i].sort(key=get_hand_value)

hand_rank = 0
total_winnings = 0

for hands in hands_ordered:
    for hand in hands:
        hand_rank = hand_rank + 1
        print("rank: "+str(hand_rank)+" hand: " + hand+ " bid: " + hand_bid_dict[hand])
        total_winnings = total_winnings + (hand_rank * int(hand_bid_dict[hand]))
print(hands_ordered)
print(total_winnings)





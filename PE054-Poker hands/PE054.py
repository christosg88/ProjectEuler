# In the card game poker, a hand consists of five cards and are ranked, from
# lowest to highest, in the following way:
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
# If two players have the same ranked hands then the rank made up of the
# highest value wins; for example, a pair of eights beats a pair of fives (see
# example 1 below). But if two ranks tie, for example, both players have a
# pair of queens, then highest cards in each hand are compared (see example 4
# below); if the highest cards tie then the next highest cards are compared,
# and so on.
# The file, poker.txt, contains one-thousand random hands dealt to two
# players. Each line of the file contains ten cards (separated by a single
# space): the first five are Player 1's cards and the last five are Player 2's
# cards. You can assume that all hands are valid (no invalid characters or
# repeated cards), each player's hand is in no specific order, and in each
# hand there is a clear winner.
# How many hands does Player 1 win?



def bestCase(numberHand, typeHand):
    one_pair = -1
    two_pairs = -1
    three_of_a_kind = -1
    straight = -1
    flush = -1
    full_house = -1
    four_of_a_kind = -1
    straight_flush = -1
    royal_flush = -1

    # High Card: Highest value card.
    high_card = numberHand[0]

    # One Pair: Two cards of the same value.
    number = 14
    while number > 1:
        if numberHand.count(number) == 2:
            one_pair = number
            straight = 0
            flush = 0
            four_of_a_kind = 0
            straight_flush = 0
            royal_flush = 0
            break
        number -= 1

    # Two Pairs: Two different pairs.
    if one_pair > 2:
        number -= 1
        while number > 1:
            if numberHand.count(number) == 2:
                two_pairs = number
                three_of_a_kind = 0
                full_house = 0
                break
            number -= 1

    # Three of a Kind: Three cards of the same value.
    if three_of_a_kind == -1:
        number = 14
        while number > 1:
            if numberHand.count(number) == 3:
                three_of_a_kind = number
                straight = 0
                flush = 0
                four_of_a_kind = 0
                straight_flush = 0
                royal_flush = 0
                break
            number -= 1

    # Straight: All cards are consecutive values.
    if straight == -1:
        number = high_card
        for card in numberHand:
            if card != number:
                straight = 0
                break
            number -= 1
        if number == high_card-5:
            straight = high_card
            full_house = 0
            four_of_a_kind = 0

    # Flush: All cards of the same suit.
    if flush == -1:
        suit = typeHand[0]
        for card in typeHand:
            if card != suit:
                flush = 0
                break
        if flush == -1:
            flush = high_card
            full_house = 0
            four_of_a_kind = 0

    # Full House: Three of a kind and a pair.
    if full_house == -1 and one_pair >= 2 and three_of_a_kind >= 2:
        full_house = three_of_a_kind

    # Four of a Kind: Four cards of the same value.
    if four_of_a_kind == -1:
        number = 14
        while number > 1:
            if numberHand.count(number) == 4:
                four_of_a_kind = number
                straight_flush = 0
                royal_flush = 0
                break
            number -= 1

    # Straight Flush: All cards are consecutive values of same suit.
    if straight_flush == -1 and flush >= 2 and straight >= 2:
        straight_flush = high_card

    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    if royal_flush == -1 and straight_flush >= 2 and high_card == 14:
        royal_flush = 1

    array = [royal_flush, straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pairs, one_pair, high_card]
    for i in xrange(len(array)):
        if array[i] == -1:
            array[i] = 0
    return array

with open("poker.txt", "r") as pocker:
    count = 0
    for l in xrange(1000):
        both_hands = pocker.readline().strip("\n").replace(" ", "")
        
        n = 0
        numberHand1 = []
        numberHand2 = []
        typeHand1 = []
        typeHand2 = []
        while n < len(both_hands)/2:
            numberHand1.append(both_hands[n])
            typeHand1.append(both_hands[n+1])
            n += 2
        while n < len(both_hands):
            numberHand2.append(both_hands[n])
            typeHand2.append(both_hands[n+1])
            n += 2

        handlength = len(both_hands)/4

        for x in xrange(handlength):
            if not numberHand1[x].isdigit():
                if numberHand1[x] == 'T':
                    numberHand1[x] = '10'
                elif numberHand1[x] == 'J':
                    numberHand1[x] = '11'
                elif numberHand1[x] == 'Q':
                    numberHand1[x] = '12'
                elif numberHand1[x] == 'K':
                    numberHand1[x] = '13'
                else:
                    numberHand1[x] = '14'
            if not numberHand2[x].isdigit():
                if numberHand2[x] == 'T':
                    numberHand2[x] = '10'
                elif numberHand2[x] == 'J':
                    numberHand2[x] = '11'
                elif numberHand2[x] == 'Q':
                    numberHand2[x] = '12'
                elif numberHand2[x] == 'K':
                    numberHand2[x] = '13'
                else:
                    numberHand2[x] = '14'

        numberHand1 = map(int, numberHand1)
        numberHand2 = map(int, numberHand2)

        while True:
            newn = 0
            for i in xrange(1, handlength):
                if numberHand1[i-1] < numberHand1[i]:
                    temp = numberHand1[i-1]
                    numberHand1[i-1] = numberHand1[i]
                    numberHand1[i] = temp
                    temp = typeHand1[i-1]
                    typeHand1[i-1] = typeHand1[i]
                    typeHand1[i] = temp
                    newn = i
            n = newn
            if n == 0:
                break

        while True:
            newn = 0
            for i in xrange(1, handlength):
                if numberHand2[i-1] < numberHand2[i]:
                    temp = numberHand2[i-1]
                    numberHand2[i-1] = numberHand2[i]
                    numberHand2[i] = temp
                    temp = typeHand2[i-1]
                    typeHand2[i-1] = typeHand2[i]
                    typeHand2[i] = temp
                    newn = i
            n = newn
            if n == 0:
                break

        
        if bestCase(numberHand1, typeHand1) > bestCase(numberHand2, typeHand2):
            count += 1
    print count
# 376
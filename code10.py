#Ask 10

import random

# getting the number of players
numhands = int(input("Give the number of players: "))

# checking that the number of players is from 2 to 6
while numhands<2 or numhands>6:
    numhands = int(input("Give the number of players: "))

deck = [
    [2, "S"], [3, "S"], [4, "S"], [5, "S"], [6, "S"], [7, "S"], [8, "S"], [9, "S"], [10, "S"], ["J", "S"], ["Q", "S"], ["K", "S"], ["A", "S"],
    [2, "C"], [3, "C"], [4, "C"], [5, "C"], [6, "C"], [7, "C"], [8, "C"], [9, "C"], [10, "C"], ["J", "C"], ["Q", "C"], ["K", "C"], ["A", "C"],
    [2, "D"], [3, "D"], [4, "D"], [5, "D"], [6, "D"], [7, "D"], [8, "D"], [9, "D"], [10, "D"], ["J", "D"], ["Q", "D"], ["K", "D"], ["A", "D"],
    [2, "H"], [3, "H"], [4, "H"], [5, "H"], [6, "H"], [7, "H"], [8, "H"], [9, "H"], [10, "H"], ["J", "H"], ["Q", "H"], ["K", "H"], ["A", "H"],
]

# shuffling the deck
random.shuffle(deck)

counter = 0
hand = []

# dealing the cards to each player
for i in range(numhands):
    hand.append([])
    for j in range(5):
        hand[i].append(deck[counter])
        counter += 1
    print(hand[i], "Player ", i+1, "hand")

# changing the figures to numbers so that it is easier to work with the hands
for i in range(numhands):
    for j in range(5):
        if hand[i][j][0] == "J":
            hand[i][j][0] = 11
        if hand[i][j][0] == "Q":
            hand[i][j][0] = 12
        if hand[i][j][0] == "K":
            hand[i][j][0] = 13
        if hand[i][j][0] == "A":
            hand[i][j][0] = 14

# putting the cards of each player in order
for i in range(numhands):
    for j in range(4, 0, -1):
        for l in range(j):
            if hand[i][l][0] > hand[i][l+1][0]:
                hand[i][l],hand[i][l+1] = hand[i][l+1],hand[i][l]

power = []
comb = []

# giving each hand a power number according to the best combination of the cards
dup = []
for i in range(numhands):
    power.append(1)
    counter = 0
    steps = 0
    suits = 0
    for j in range(4):
        if hand[i][j][0] == hand[i][j+1][0]:
            counter += 1
            if counter == 1: #checking for duplicate cards
                dup.append(hand[i][j][0])
            elif hand[i][j-1][0] != hand[i][j][0]:
                dup.append(hand[i][j][0])
        if hand[i][j][0]+1 == hand[i][j+1][0]: #checking for straight cards
            steps += 1
        if hand[i][j][1] == hand[i][j+1][1]: #checking for same suit cards
            suits += 1
    if len(dup) == 1 and counter == 3: #four of a kind
        power[i] = 8
    elif len(dup) == 2 and counter == 3: #full house
        power[i] = 7
    elif len(dup) == 1 and counter == 2: #three of a kind
        power[i] = 4
    elif len(dup) == 2 and counter == 2: #two pairs
        power[i] = 3
    elif len(dup) == 1 and counter == 1: #one pair
        power[i] = 2
    elif steps == 4 and suits ==4: #straight flush
        power[i] = 9
    elif steps == 4: #straight
        power[i] = 5
    elif suits == 4: #flush
        power[i] = 6
    dup.clear()

# getting the highest power number of the hands
best = []
max = power[0]
for i in range(numhands):
    if power[i] > max:
        max = power[i]

# inserting into the list best the index of the hands with the highest power number
for i in range(numhands):
    if power[i] == max:
        best.append(i)

# if more than one hands have the highest power number procedes to compare the hands with the highest power number 
if len(best) > 1:
    if max == 1: # comparing the hands if the power number is 1
        out = []
        for i in range(len(best)):
            k = 1
            for l in range(k, len(best)):
                k += 1
                for j in range(4, -1, -1):
                    if hand[best[i]][j][0] > hand[best[l]][j][0]:
                        out.append(best[l])
                        break
                    elif hand[best[i]][j][0] < hand[best[l]][j][0]:
                        out.append(best[i]) 
                        break
            if len(out) > 0:
                for j in out:
                        hand[j][0][0] = -1
                out.clear()
    elif max == 2: # comparing the hands if the power number is 2
        pair = []
        kicker = []
        out = []
        for i in range(len(best)):
            kicker.append([])
            for j in range(4):
                if hand[best[i]][j][0] == hand[best[i]][j + 1][0]:
                    pair.append(hand[best[i]][j][0])
                    break
            for j in range(5):
                if hand[best[i]][j][0] != pair[i]:
                    kicker[i].append(hand[best[i]][j][0])
        for i in range(len(best)):
            for j in range(len(best)):
                if pair[i] > pair[j]:
                    out.append(best[j])
                elif pair[i] < pair[j]:
                    out.append(best[i])
            if len(out) > 0:
                for j in out:
                    hand[j][0][0] = -1
                out.clear()
        for i in range(len(best)):
            for l in range(len(best)-1, -1, -1):
                for j in range(2, -1, -1):
                    if hand[best[i]][0][0] != -1 and hand[best[l]][0][0] != -1:
                       if kicker[i][j] > kicker[l][j]:
                            out.append(best[l])
                            break
                       elif kicker[i][j] < kicker[l][j]:
                            out.append(best[i])
                            break
            for j in out:
               hand[j][0][0] = -1
            out.clear()
    elif max == 3: # comparing the hands if the power number is 3
        pair = []
        kicker = []
        out = []
        for i in range(len(best)):
            pair.append([])
            for j in range(4):
                if hand[best[i]][j][0] == hand[best[i]][j+1][0]:
                    pair[i].append(hand[best[i]][j][0])
            for j in range(5):
                if pair[i][0] != hand[best[i]][j][0] and pair[i][1] != hand[best[i]][j][0]:
                    kicker.append(hand[best[i]][j][0])
        for i in range(len(best)):
            for j in range(len(best)):
                if pair[i][1] > pair[j][1]:
                    out.append(best[j])
                elif pair[i][1] < pair[j][1]:
                    out.append(best[i])
                elif pair[i][1] == pair[j][1]:
                    if pair[i][0] < pair[j][0]:
                        out.append(best[i])
                    elif pair[i][0] > pair[j][0]:
                        out.append(best[j])
                if len(out) > 0:
                    for l in out:
                        hand[l][0][0] = -1
                    out.clear()
        out.clear()
        for i in range(len(best)):
                for j in range(len(best)):
                    if hand[best[i]][0][0] != -1 and hand[best[j]][0][0] != -1:
                        if kicker[i] > kicker[j]:
                            out.append(best[j])
                            break
                        elif kicker[i] < kicker[j]:
                            out.append(best[i])
                            break
        if len(out) > 0:
            for i in out:
                hand[i][0][0] = -1
    elif max == 4: # comparing the hands if the power number is 4
        triple = []
        out = []
        for i in range(len(best)):
            for j in range(4):
                if hand[best[i]][j][0] == hand[best[i]][j+1][0]:
                    triple.append(hand[best[i]][j][0])
                    break
        for i in range(len(best)):
            for j in range(len(best)):
                if triple[i] > triple[j]:
                    out.append(best[j])
                elif triple[i] < triple[j]:
                    out.append(best[i])
            if len(out) > 0:
                for j in out:
                    hand[j][0][0] = -1
                out.clear()
    elif max == 5: # comparing the hands if the power number is 5
        out = []
        for i in best:
            for j in best:
                if hand[i][0][0] > hand[j][0][0]:
                    out.append(j)
                elif hand[i][0][0] < hand[j][0][0]:
                    out.append(i)
            if len(out) > 0:
                for j in out:
                    hand[j][0][0] = -1
                out.clear()
    elif max == 6: # comparing the hands if the power number is 6
        out = []
        for i in range(len(best)):
            k = 1
            for l in range(k, len(best)):
                k += 1
                for j in range(4, -1, -1):
                    if hand[best[i]][j][0] > hand[best[l]][j][0]:
                        out.append(best[l])
                        break
                    elif hand[best[i]][j][0] < hand[best[l]][j][0]:
                        out.append(best[i])
                        break
            if len(out) > 0:
                for j in out:
                        hand[j][0][0] = -1
                out.clear()
    elif max == 7: # comparing the hands if the power number is 7
        out = []
        triple = []
        double = []
        for i in range(len(best)):
            counter = 0
            for j in range(4):
                if hand[best[i]][j][0] == hand[best[i]][j+1][0]:
                    counter += 1
                elif hand[best[i]][j][0] != hand[best[i]][j+1][0]:
                    if counter == 1:
                        double.append(hand[best[i]][j][0])
                        triple.append(hand[best[i]][j+1][0])
                        break
                    elif counter == 2:
                        double.append(hand[best[i]][j+1][0])
                        triple.append(hand[best[i]][j][0])
                        break
        for i in range(len(best)):
            for j in range(len(best)):
                if triple[i] > triple[j]:
                    out.append(best[j])
                elif triple[i] < triple[j]:
                    out.append(best[i])
            if len(out) > 0:
                for j in out:
                    hand[j][0][0] = -1
                out.clear()
        for i in range(len(best)):
            for j in range(len(best)):
                if hand[best[i]][0][0] != -1 and hand[best[j]][0][0] != -1:
                    if double[i] > double[j]:
                        out.append(best[j])
                    elif double[i] < double[j]:
                        out.append(best[i])
            if len(out) > 0:
                for j in out:
                    hand[j][0][0] = -1
                out.clear()
    elif max == 8: # comparing the hands if the power number is 8
        quad = []
        kicker = []
        out = []
        for i in range(len(best)):
            for j in range(4):
                if hand[best[i]][j][0] == hand[best[i]][j+1][0]:
                    quad.append(hand[best[i]][j][0])
                    break
            for j in range(5):
                if quad[i] != hand[best[i]][j][0]:
                    kicker.append(hand[best[i]][j][0])
                    break
        for i in range(len(best)):
            for j in range(len(best)):
                if quad[i] > quad[j]:
                    out.append(best[j])
                elif quad[i] < quad[j]:
                    out.append(best[i])
            if len(out) > 0:
                for j in out:
                    hand[j][0][0] = -1
                out.clear()
        for i in range(len(best)):
            for j in range(len(best)):
                if hand[best[i]][0][0] != -1 and hand[best[j]][0][0] != -1:
                    if kicker[i] > kicker[j]:
                        out.append(best[j])
                    elif kicker[i] < kicker[j]:
                        out.append(best[i])
            if len(out) > 0:
                for j in out:
                    hand[j][0][0] = -1
                out.clear()
    elif max == 9: # comparing the hands if the power number is 9
        out = []
        for i in best:
            for j in best:
                if hand[i][0][0] > hand[j][0][0]:
                    out.append(j)
                elif hand[i][0][0] < hand[j][0][0]:
                    out.append(i)
            if len(out) > 0:
                for j in out:
                    hand[j][0][0] = -1
                out.clear()

# changing the cards with numbers 11 and up to figures so they could be displayed
for i in best:
    for j in range(5):
        if hand[i][j][0] == 11:
            hand[i][j][0] = "J"
        if hand[i][j][0] == 12:
            hand[i][j][0] = "Q"
        if hand[i][j][0] == 13:
            hand[i][j][0] = "K"
        if hand[i][j][0] == 14:
            hand[i][j][0] = "A"

# printing the highest power number
print(power)

# printing the best hands
if len(best) == 1: # if there is one best hand
    print("The winner is player ", best[0]+1)
    print("Hand")
    print(hand[best[0]])
else: # if there are more than one best hands
    print("The winners are players :")
    for i in best:
        if hand[i][0][0] != -1:
            print(i+1)
    for i in best:
        if hand[i][0][0] != -1:
            print("Hand ", i+1)
            print(hand[i])
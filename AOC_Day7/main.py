from collections import Counter
def load_strings():
    tab = []
    with open("input.txt", "r") as file:
        for index, line_content in enumerate(file, start=0):
            line_content = line_content[:-1]
            tab.append(line_content)
    return tab


def get_dict(hand):
    hand_dict = {}
    for char in hand:
        if char in hand_dict:
            hand_dict[char] += 1
        else:
            hand_dict[char] = 1
    return hand_dict


def get_power_level(dicted_hand):
    as_list = list(dicted_hand.values())
    if max(dicted_hand.values()) == 5:
        return 7
    elif max(dicted_hand.values()) == 4:
        return 6
    elif Counter(as_list) == Counter([2, 3]):
        return 5
    elif Counter(as_list) == Counter([3, 1, 1]):
        return 4
    elif Counter(as_list) == Counter([2, 2, 1]):
        return 3
    elif Counter(as_list) == Counter([2, 1, 1, 1]):
        return 2
    return 1


def get_letter_level(letter):
    letters = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    for g in range(len(letters)):
        if letter == letters[g]:
            return g


def compare_hands(h1, h2):

    if h1[1] < h2[1]:
        return True
    elif h1[1] == h2[1]:
        for i in range(len(h1[0])):
            if get_letter_level(h1[0][i]) < get_letter_level(h2[0][i]):
                return True
            elif get_letter_level(h1[0][i]) > get_letter_level(h2[0][i]):
                return False
    return False


def sort_hands(hands_with_levels, bids):
    for g in range(len(hands_with_levels) - 1):
        for j in range(g + 1, len(hands_with_levels)):
            if compare_hands(hands_with_levels[g], hands_with_levels[j]):
                hands_with_levels[g], hands_with_levels[j] = hands_with_levels[j], hands_with_levels[g]
                bids[g], bids[j] = bids[j], bids[g]
    return hands_with_levels


def get_hands_and_dicts(tab):
    hands = []
    bids = []
    power_levels = []
    for line in tab:
        line = line.split()
        hands.append(line[0])
        bids.append(line[1])
        power_levels.append(get_power_level(get_dict(line[0])))
    hands_with_levels = list(zip(hands, power_levels))
    hands_with_levels = sort_hands(hands_with_levels, bids)
    total = 0
    for g in range(len(bids)):
        total += (len(bids)-g) * int(bids[g])
    print(total)


lines = load_strings()
get_hands_and_dicts(lines)

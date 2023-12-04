def load_strings():
    tab = []
    with open("input.txt", "r") as file:
        for index, line_content in enumerate(file, start=0):
            line_content = line_content[:-1]
            line_content = line_content[10:]
            tab.append(line_content)
    return tab


def check_card(card):
    card = card.split('|')
    winners = card[0].split()
    yours = card[1].split()
    duplicates = 0
    for your_card in yours:
        if your_card in winners:
            duplicates += 1
            winners.remove(your_card)
    if duplicates != 0:
        return duplicates
    return 0

def add_reps(index, amount, how_many_times, reps):

    for g in range(amount):
        if index + g < len(reps):
            reps[index+g] += how_many_times
        else:
            break
    return reps

def sum_cards(tab, reps):
    total = 0
    for g in range(len(tab)):
        to_add = check_card(tab[g])
        if to_add != 0:
            reps = add_reps(g+1, to_add, reps[g], reps)
        total += reps[g]
    print(total)


lines = load_strings()
repeats = [1] * len(lines)
sum_cards(lines, repeats)

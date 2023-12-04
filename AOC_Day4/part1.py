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
        return int(pow(2, duplicates - 1))
    return 0

def sum_cards(tab):
    total = 0
    for g in range(len(tab)):
        total += check_card(tab[g])
    print(total)


lines = load_strings()
sum_cards(lines)

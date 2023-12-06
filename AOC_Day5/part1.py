def load_strings():
    tab = []
    with open("input.txt", "r") as file:
        for index, line_content in enumerate(file, start=0):
            line_content = line_content[:-1]
            tab.append(line_content)
    return tab


def load_seeds(line):
    line = line[7:].split()
    return [int(x) for x in line]


def load_map(tab, starting_index):
    to_return = []
    for g in range(len(tab)):
        if g + starting_index >= len(tab) or tab[g + starting_index] == "":
            break
        else:
            to_return.append(tab[g + starting_index])
    return to_return


def get_maps(tab):
    current_number = 0
    loaded_maps = []
    for g in range(len(tab)):
        if 'map:' in tab[g]:
            loaded_maps.append(load_map(tab, g + 1))
            current_number += 1
        elif current_number == 7:
            break
    return loaded_maps


def check_seed(s, m):
    for line in m:
        line = line.split()
        limit = int(line[1]) + int(line[2]) - 1
        start = int(line[1])
        if start <= s <= limit:
            s = int(line[0]) + (s - start)
            break
    return s


def map_seeds(s, m):
    for i in range(len(m)):
        for j in range(len(s)):
            s[j] = check_seed(s[j], m[i])

lines = load_strings()
seeds = load_seeds(lines[0])
maps = get_maps(lines)
map_seeds(seeds, maps)
print(min(seeds))

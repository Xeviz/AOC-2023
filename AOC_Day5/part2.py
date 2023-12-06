import copy
def load_strings():
    tab = []
    with open("input.txt", "r") as file:
        for index, line_content in enumerate(file, start=0):
            line_content = line_content[:-1]
            tab.append(line_content)
    return tab


def load_seeds(line):
    line = line[7:].split()
    unpaired = [int(x) for x in line]
    paired = []
    for i in range(0, len(unpaired), 2):
        paired.append([])

        paired[int(i / 2)].append(unpaired[i])
        paired[int(i / 2)].append(unpaired[i])
        paired[int(i / 2)].append(unpaired[i + 1])

    return paired


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


def check_seed_range(seeds_line, m, s):
    current_map = copy.deepcopy(m)
    for line in m:
        current_map.remove(line)
        line = line.split()
        m_range = int(line[2])
        limit = int(line[1]) + int(line[2]) - 1
        start = int(line[1])
        if start <= seeds_line[0] <= limit and start + seeds_line[2] <= limit:
            seeds_line[0] = int(line[0]) + seeds_line[0] - start
            return seeds_line
        elif start <= seeds_line[0] <= limit < seeds_line[0] + seeds_line[2]:
            new_seeds_line = [seeds_line[0] + int(line[2]), seeds_line[1] + int(line[2]), seeds_line[2] - int(line[2])]
            seeds_line[0] = int(line[0]) + (seeds_line[0] - start)
            seeds_line[1] = seeds_line[1]
            seeds_line[2] = int(line[2])
            s.append(check_seed_range(new_seeds_line, current_map, s))
            return seeds_line
        elif seeds_line[0] < start <= seeds_line[0] + seeds_line[2] <= limit:
            new_seeds_line = [seeds_line[0], seeds_line[1], start - seeds_line[0]]

            seeds_line[0] = int(line[0])
            seeds_line[1] += new_seeds_line[2]
            seeds_line[2] -= new_seeds_line[2]
            s.append(check_seed_range(new_seeds_line, current_map, s))
            return seeds_line
        elif seeds_line[0] < start and seeds_line[0] + seeds_line[2] > limit:

            new_seeds_line_1 = [seeds_line[0], seeds_line[1], start - seeds_line[0]]
            new_seeds_line_2 = [seeds_line[0] + m_range + new_seeds_line_1[2], seeds_line[1] + m_range + new_seeds_line_1[2], seeds_line[2] - m_range - new_seeds_line_1[2]]

            seeds_line[0] = int(line[0])
            seeds_line[1] += new_seeds_line_1[2]
            seeds_line[2] = m_range
            s.append(check_seed_range(new_seeds_line_1, current_map, s))
            s.append(check_seed_range(new_seeds_line_2, current_map, s))
            return seeds_line
    return seeds_line


def map_seeds(s, m):
    for i in range(len(m)):
        for j in range(len(s)):
            s[j] = check_seed_range(s[j], m[i], s)


def get_locations(tab):
    locations = []
    for g in range(len(tab)):
        locations.append(tab[g][0])
    print(min(locations))


lines = load_strings()
seed_maps = load_seeds(lines[0])
maps = get_maps(lines)
map_seeds(seed_maps, maps)
get_locations(seed_maps)

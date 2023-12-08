def load_strings():
    tab = []
    with open("input.txt", "r") as file:
        for index, line_content in enumerate(file, start=0):
            line_content = line_content[:-1]
            tab.append(line_content)
    return tab


def search_for_source(tab, source):
    for i in range(len(tab)):
        if tab[i] == source:
            return i

def load_map(tab, loop_pattern):
    sources = []
    lefts = []
    rights = []

    for line in tab:
        sources.append(line[0] + line[1] + line[2])
        lefts.append(line[7] + line[8] + line[9])
        rights.append(line[12] + line[13] + line[14])

    moves = 0
    g = search_for_source(sources, 'AAA')
    while sources[g] != 'ZZZ':
        for j in range(len(loop_pattern)):
            if loop_pattern[j] == 'L':
                g = search_for_source(sources, lefts[g])
            else:
                g = search_for_source(sources, rights[g])
            moves += 1
            if sources[g] == 'ZZZ':
                return moves


lines = load_strings()
loop = lines.pop(0)
lines.remove(lines[0])
print(load_map(lines, loop))

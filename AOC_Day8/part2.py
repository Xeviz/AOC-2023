import math

def load_strings():
    tab = []
    with open("input.txt", "r") as file:
        for index, line_content in enumerate(file, start=0):
            line_content = line_content[:-1]
            tab.append(line_content)
    return tab

def search_for_a(tab):
    a_tab = []
    for line in tab:
        if 'A' in line:
            a_tab.append(line)
    return a_tab

def go_direction(source, paths, direction):
    return paths[source + direction]

def move_all(sources, paths, direction):
    for i in range(len(sources)):
        sources[i] = go_direction(sources[i], paths, direction)
    return sources

def search_lcm(values):
    while len(values) != 1:
        values[0] = math.lcm(values[0], values[1])
        values.pop(1)
    return values[0]

def load_map(tab, loop_pattern):
    sources = []
    paths = {}

    for line in tab:
        sources.append(line[0] + line[1] + line[2])
        paths[line[0] + line[1] + line[2] + 'L'] = line[7] + line[8] + line[9]
        paths[line[0] + line[1] + line[2] + 'R'] = line[12] + line[13] + line[14]

    g = search_for_a(sources)
    distances = [0] * len(g)
    moves = 0
    while 0 in distances:
        for j in range(len(loop_pattern)):
            moves += 1
            move_all(g, paths, loop_pattern[j])
            for a in range(len(g)):
                if 'Z' in g[a] and distances[a] == 0:
                    distances[a] = moves
    print(search_lcm(distances))


lines = load_strings()
loop = lines.pop(0)
lines.remove(lines[0])
load_map(lines, loop)

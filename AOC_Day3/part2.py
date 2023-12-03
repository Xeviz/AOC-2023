def load_strings():
    tab = []
    with open("input.txt", "r") as file:
        for index, line_content in enumerate(file, start=0):
            line_content = line_content[:-1]
            tab.append(line_content)
    return tab
def extract_number(tab, y, x):
    number = ""
    starting_index = x
    for z in range(len(tab[y])):
        if (x - z >= 0) and ('0' <= tab[y][x - z] <= '9'):
            continue
        else:
            starting_index = x - z + 1
            break

    for z in range(len(tab[y])):
        if (starting_index + z < len(tab[y])) and ('0' <= tab[y][starting_index + z] <= '9'):
            number += tab[y][starting_index + z]
        else:
            break
    return number


def check_star_neighbours(tab, y, x):
    neighbours = []
    current = ""
    if '0' <= tab[y - 1][x - 1] <= '9':
        current = extract_number(tab, y - 1, x - 1)
        neighbours.append(int(current))
    elif (current == "") and ('0' <= tab[y - 1][x] <= '9'):
        current = extract_number(tab, y - 1, x)
        neighbours.append(int(current))
    if (tab[y - 1][x] < '0' or tab[y - 1][x] > '9') and ('0' <= tab[y - 1][x + 1] <= '9'):
        current = extract_number(tab, y - 1, x + 1)
        neighbours.append(int(current))

    current = ""
    if '0' <= tab[y + 1][x - 1] <= '9':
        current = extract_number(tab, y + 1, x - 1)
        neighbours.append(int(current))
    elif (current == "") and ('0' <= tab[y + 1][x] <= '9'):
        current = extract_number(tab, y + 1, x)
        neighbours.append(int(current))
    if (tab[y + 1][x] < '0' or tab[y + 1][x] > '9') and ('0' <= tab[y + 1][x + 1] <= '9'):
        current = extract_number(tab, y + 1, x + 1)
        neighbours.append(int(current))

    if '0' <= tab[y][x - 1] <= '9':
        current = extract_number(tab, y, x - 1)
        neighbours.append(int(current))
    if '0' <= tab[y][x + 1] <= '9':
        current = extract_number(tab, y, x + 1)
        neighbours.append(int(current))

    if len(neighbours) == 2:
        return neighbours[0] * neighbours[1]
    else:
        return 0

def find_stars(tab):
    to_add = 0
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == '*':
                to_add += check_star_neighbours(tab, i, j)
    return to_add


lines = load_strings()
total = find_stars(lines)
print(total)

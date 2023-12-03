def load_strings():
    tab = []
    with open("input.txt", "r") as file:
        for index, line_content in enumerate(file, start=0):
            line_content = line_content[:-1]
            tab.append(line_content)
    return tab


def check_pos(y, x, tab):
    if (48 <= ord(tab[y][x]) <= 57) or (ord(tab[y][x]) == 46):
        return False
    return True


def check_neighbours(y, x, length, tab, y_indexes, x_indexes):
    current_x = x
    for j in range(length):
        if (y - 1 >= 0 and current_x - 1 >= 0) and check_pos(y - 1, current_x - 1, tab):
            return True
        elif (y + 1 < y_indexes and current_x - 1 >= 0) and check_pos(y + 1, current_x - 1, tab):
            return True
        elif (y - 1 >= 0 and current_x + 1 < x_indexes) and check_pos(y - 1, current_x + 1, tab):
            return True
        elif (y + 1 < y_indexes and current_x + 1 < x_indexes) and check_pos(y + 1, current_x + 1, tab):
            return True
        elif (y - 1 >= 0) and check_pos(y - 1, current_x, tab):
            return True
        elif (y + 1 < y_indexes) and check_pos(y + 1, current_x, tab):
            return True
        elif (current_x - 1 >= 0) and check_pos(y, current_x - 1, tab):
            return True
        elif (current_x + 1 < x_indexes) and check_pos(y, current_x + 1, tab):
            return True
        current_x += 1
    return False


def find_number(tab, y, x):
    if x >= len(tab[0]):
        return 0
    number = ""
    length = 0
    to_return = 0
    for z in range(len(tab[y])):
        if (x+z < len(tab[y])) and ('0' <= tab[y][x + z] <= '9'):
            number += tab[y][x + z]
        else:
            length = z + 1
            break
    if check_neighbours(y, x, length - 1, tab, len(tab), len(tab[0])):
        to_return += int(number)
    x += length
    for z in range(len(tab[y])):
        if x >= len(tab[y]):
            break
        elif tab[y][x] == '.':
            x += 1
    return to_return + find_number(tab, y, x)


lines = load_strings()
total = 0
for g in range(len(lines)):
    total += find_number(lines, g, 0)
print(total)

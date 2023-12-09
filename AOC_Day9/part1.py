def load_strings():
    tab = []
    with open("input.txt", "r") as file:
        for index, line_content in enumerate(file, start=0):
            line_content = line_content[:-1]
            tab.append(line_content)
    return tab


def check_line(line):

    new_line = []
    for g in range(len(line)-1):
        new_line.append(line[g+1]-line[g])
    return new_line

def check_all_sub_lines(starting_line):

    dif_tab = [starting_line]
    current = 0
    while not dif_tab or sum(dif_tab[current]) != 0:
        current += 1
        dif_tab.append([])
        dif_tab[current] = check_line(dif_tab[current-1])
    dif_tab[current].append(0)

    for g in range(current+1):
        dif_tab[current-1-g].append(dif_tab[current-1-g][-1] + dif_tab[current-g][-1])
    return dif_tab[0][-1]

def convert_to_ints(line):
    line = line.split()
    as_int = []
    for g in range(len(line)):
        as_int.append(int(line[g]))
    return as_int

def get_all_vals(tab):
    total = 0
    for line in tab:
        val = convert_to_ints(line)
        total += check_all_sub_lines(val)
    print(total)


lines = load_strings()
get_all_vals(lines)

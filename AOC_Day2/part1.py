import re

MAX_RED, MAX_GREEN, MAX_BLUE = 12, 13, 14


def load_strings():
    tab = []
    with open("input.txt", "r") as file:
        for index, line_content in enumerate(file, start=0):
            if index != 99:
                line_content = line_content[:-1]
            tab.append(line_content)
    return tab


def check_patterns(singles):
    pattern_red = r" (\d+) red"
    pattern_green = r" (\d+) green"
    pattern_blue = r" (\d+) blue"

    for x in range(len(singles)):
        match = re.search(pattern_red, singles[x])
        if match is not None and int(match.group(1)) > MAX_RED:
            return True
        elif match is not None:
            continue

        match = re.search(pattern_green, singles[x])
        if match is not None and int(match.group(1)) > MAX_GREEN:
            return True
        elif match is not None:
            continue

        match = re.search(pattern_blue, singles[x])
        if match is not None and int(match.group(1)) > MAX_BLUE:
            return True
        elif match is not None:
            continue


def check_line(line, game_id):
    line = line.split(';')
    line[0] = line[0][7:]
    amount = len(line)

    for g in range(amount):
        singles = line[g].split(',')
        if check_patterns(singles):
            return 0
    return game_id


lines = load_strings()
total = 0
for g in range(100):
    total += check_line(lines[g], g+1)

print(total)

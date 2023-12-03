import re

def load_strings():
    tab = []
    with open("input.txt", "r") as file:
        for index, line_content in enumerate(file, start=0):
            if index != 99:
                line_content = line_content[:-1]
            tab.append(line_content)
    return tab


def check_patterns(singles, red, green, blue):
    pattern_red = r" (\d+) red"
    pattern_green = r" (\d+) green"
    pattern_blue = r" (\d+) blue"
    for x in range(len(singles)):
        match = re.search(pattern_red, singles[x])
        if match is not None and int(match.group(1)) > red:
            red = int(match.group(1))
        elif match is not None:
            continue

        match = re.search(pattern_green, singles[x])
        if match is not None and int(match.group(1)) > green:
            green = int(match.group(1))
        elif match is not None:
            continue

        match = re.search(pattern_blue, singles[x])
        if match is not None and int(match.group(1)) > blue:
            blue = int(match.group(1))
        elif match is not None:
            continue
    return [red, green, blue]


def check_line(line, game_id):
    line = line.split(';')
    line[0] = line[0][7:]
    amount = len(line)
    local_rgb = [0, 0, 0]

    for g in range(amount):
        singles = line[g].split(',')
        local_rgb = check_patterns(singles, local_rgb[0], local_rgb[1], local_rgb[2])
    return local_rgb[0]*local_rgb[1]*local_rgb[2]


lines = load_strings()
total = 0
for g in range(100):
    total += check_line(lines[g], g+1)

print(total)

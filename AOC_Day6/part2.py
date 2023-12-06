def load_strings():
    tab = []
    with open("input.txt", "r") as file:
        for index, line_content in enumerate(file, start=0):
            line_content = line_content[:-1]
            line_content = line_content[11:]
            tab.append(line_content)
    return tab

def check_race(time, distance):
    options = 0
    for i in range(time):
        if i*(time-i) > distance:
            options += 1
    return options


lines = load_strings()
one_time = ""
for x in lines[0].split():
    one_time += x
one_distance = ""
for x in lines[0].split():
    one_distance += x
print(check_race(int(one_time), int(one_distance)))


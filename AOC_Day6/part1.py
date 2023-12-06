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

def check_all_races(t, d):
    options = 1
    for i in range(len(t)):
        options *= check_race(int(t[i]), int(d[i]))
    print(options)


lines = load_strings()
times = lines[0].split()
distances = lines[1].split()
check_all_races(times, distances)

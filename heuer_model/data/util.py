data = dict()
with open("hometeam.csv", "r") as h_source_file:
    for line in h_source_file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            continue

        elements = line.split(";")
        if elements[0] not in data.keys():
            data[elements[0]] = {}
        if elements[1] not in data[elements[0]].keys():
            data[elements[0]][elements[1]] = {}
        if elements[2] not in data[elements[0]][elements[1]].keys():
            data[elements[0]][elements[1]][elements[2]] = {}
        if elements[3] not in data[elements[0]][elements[1]][elements[2]].keys():
            data[elements[0]][elements[1]][elements[2]
                                           ][elements[3]] = elements[4]


with open("awayteam.csv", "r") as a_source_file:
    for line in a_source_file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            continue

        elements = line.split(";")
        if elements[0] not in data.keys():
            data[elements[0]] = {}
        if elements[1] not in data[elements[0]].keys():
            data[elements[0]][elements[1]] = {}
        if elements[2] not in data[elements[0]][elements[1]].keys():
            data[elements[0]][elements[1]][elements[2]] = {}
        if elements[3] not in data[elements[0]][elements[1]][elements[2]].keys():
            data[elements[0]][elements[1]][elements[2]
                                           ][elements[3]] = elements[4]


with open("teamstrength.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            print(line + ";actual_goaldiff")
            continue

        elements = line.split(";")

        actual_gd = data[elements[0]][elements[1]][elements[2]][elements[3]]

        print(line + ";" + actual_gd)

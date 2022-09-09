import numpy as np

avg_data = dict()
with open("mv_avg.csv", "r") as avg_file:
    for line in avg_file:
        if line.startswith("country"):
            continue

        line = line.replace("\n", "")
        elements = line.split(";")

        if elements[0] not in avg_data.keys():
            avg_data[elements[0]] = {}
        if elements[1] not in avg_data[elements[0]].keys():
            avg_data[elements[0]][elements[1]] = {}

        avg_data[elements[0]][elements[1]] = elements[2]


data = dict()
with open("mv.csv", "r") as file:
    for line in file:
        if line.startswith("country"):
            continue

        line = line.replace("\n", "")
        elements = line.split(";")

        if elements[0] not in data.keys():
            data[elements[0]] = {}
        if elements[1] not in data[elements[0]].keys():
            data[elements[0]][elements[1]] = 0

        if elements[0] == "GER":
            data[elements[0]][elements[1]
                              ] += np.square(float(elements[4]) - float(avg_data[elements[0]][elements[1]])) / 18
        else:
            data[elements[0]][elements[1]
                              ] += np.square(float(elements[4]) - float(avg_data[elements[0]][elements[1]])) / 20

print("country;season;ln_market_value_variance")
for a in data.keys():
    for b in data[a].keys():
        print(a + ";" + b+";" + str(data[a][b]))

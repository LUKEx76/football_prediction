import numpy as np

data = dict()
with open("avg_ln_marketvalue.csv", "r") as source_file:
    for line in source_file:
        line = line.replace("\n", "")
        elements = line.split(";")

        if elements[0] not in data.keys():
            data[elements[0]] = {}
        if elements[1] not in data[elements[0]].keys():
            data[elements[0]][elements[1]] = {}

        data[elements[0]][elements[1]] = float(elements[2])


with open("teamstrength.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            print(line + ";market_value_ln_relative")
            continue

        elements = line.split(";")

        market_value_ln_relative = np.log(
            float(elements[8]) * 1000000) - data[elements[0]][elements[1]]

        print(line + ";" + str(market_value_ln_relative))

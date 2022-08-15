# mean_data = dict()
# with open("chance_mean.csv", "r") as file:
#     for line in file:
#         line = line.replace("\n", "")

#         if line.startswith("country"):
#             # print(line + ";market_value_ln_relative")
#             continue

#         elements = line.split(";")

#         if elements[0] not in mean_data.keys():
#             mean_data[elements[0]] = {}
#         if elements[1] not in mean_data[elements[0]].keys():
#             mean_data[elements[0]][elements[1]] = {}

#         mean_data[elements[0]][elements[1]] = elements[2]

rel_data = dict()
with open("relegators_chancesum.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            continue

        elements = line.split(";")

        if elements[0] not in rel_data.keys():
            rel_data[elements[0]] = {}
        if elements[1] not in rel_data[elements[0]].keys():
            rel_data[elements[0]][elements[1]] = {}

        rel_data[elements[0]][elements[1]] = int(elements[2])

data = dict()
with open("chance.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            continue

        elements = line.split(";")

        if elements[0] not in data.keys():
            data[elements[0]] = {}
        if elements[1] not in data[elements[0]].keys():
            data[elements[0]][elements[1]] = {}
        if elements[2] not in data[elements[0]][elements[1]].keys():
            data[elements[0]][elements[1]][elements[2]] = 0

        data[elements[0]][elements[1]][elements[2]] += float(elements[3])


with open("teamstrength.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            print(line + ";past_chancesum")
            continue

        elements = line.split(";")

        chance_sum = 0

        if elements[1] == "14":
            chance_sum = float(0)
        if elements[1] == "15":
            if elements[3] not in data[elements[0]]["14"].keys():
                chance_sum = float(rel_data[elements[0]]["14"])
            else:
                chance_sum = float(data[elements[0]]["14"][elements[3]])
        if elements[1] == "16":
            if elements[3] not in data[elements[0]]["14"].keys():
                chance_sum = float(rel_data[elements[0]]["14"])
            else:
                chance_sum = float(data[elements[0]]["14"][elements[3]])
            if elements[3] not in data[elements[0]]["15"].keys():
                chance_sum += float(rel_data[elements[0]]["15"])
            else:
                chance_sum += float(data[elements[0]]["15"][elements[3]])
            chance_sum = chance_sum / 2
        if elements[1] == "17":
            if elements[3] not in data[elements[0]]["14"].keys():
                chance_sum = float(rel_data[elements[0]]["14"])
            else:
                chance_sum = float(data[elements[0]]["14"][elements[3]])
            if elements[3] not in data[elements[0]]["15"].keys():
                chance_sum += float(rel_data[elements[0]]["15"])
            else:
                chance_sum += float(data[elements[0]]["15"][elements[3]])
            if elements[3] not in data[elements[0]]["16"].keys():
                chance_sum += float(rel_data[elements[0]]["16"])
            else:
                chance_sum += float(data[elements[0]]["16"][elements[3]])
            chance_sum = chance_sum / 3
        if elements[1] == "18":
            if elements[3] not in data[elements[0]]["15"].keys():
                chance_sum = float(rel_data[elements[0]]["15"])
            else:
                chance_sum = float(data[elements[0]]["15"][elements[3]])
            if elements[3] not in data[elements[0]]["16"].keys():
                chance_sum += float(rel_data[elements[0]]["16"])
            else:
                chance_sum += float(data[elements[0]]["16"][elements[3]])
            if elements[3] not in data[elements[0]]["17"].keys():
                chance_sum += float(rel_data[elements[0]]["17"])
            else:
                chance_sum += float(data[elements[0]]["17"][elements[3]])
            chance_sum = chance_sum / 3

        print(line + ";" + str(chance_sum))

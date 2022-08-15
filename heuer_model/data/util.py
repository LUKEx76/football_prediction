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


data = dict()
with open("goal_amount.csv", "r") as file:
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
            data[elements[0]][elements[1]][elements[2]] = {}

        if elements[3] not in data[elements[0]][elements[1]][elements[2]].keys():
            data[elements[0]][elements[1]][elements[2]][elements[3]] = 0
        if elements[4] not in data[elements[0]][elements[1]][elements[2]].keys():
            data[elements[0]][elements[1]][elements[2]][elements[4]] = 0

        data[elements[0]][elements[1]][elements[2]
                                       ][elements[3]] = int(elements[5])
        data[elements[0]][elements[1]][elements[2]
                                       ][elements[4]] = int(elements[5])


with open("teamstrength.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            print(line + ";actual_goalamount")
            continue

        elements = line.split(";")

        goalamount = data[elements[0]][elements[1]][elements[2]][elements[3]]

        print(line + ";" + str(goalamount))

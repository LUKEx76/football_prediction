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
with open("teamstrength.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            # reordered and cleansed
            # print(line)
            continue

        elements = line.split(";")

        # if elements[0] == "ENG" and elements[1] == "14" and int(elements[2]) < 4:
        if elements[0] not in data.keys():
            data[elements[0]] = {}
        if elements[1] not in data[elements[0]].keys():
            data[elements[0]][elements[1]] = {}
        if elements[2] not in data[elements[0]][elements[1]].keys():
            data[elements[0]][elements[1]][elements[2]] = {}
        if elements[3] not in data[elements[0]][elements[1]][elements[2]].keys():
            data[elements[0]][elements[1]][elements[2]][elements[3]] = {}

        data[elements[0]][elements[1]][elements[2]][elements[3]] = {
            "country": elements[0],
            "season": elements[1],
            "matchnumber": elements[2],
            "teamname": elements[3],
            "curr_chancediff": elements[4],
            "past_chancediff_combined": elements[10],
            "past_chanceamount": elements[12],
            "market_value_ln_relative": elements[11],
            "actual_goalamount": elements[13],
            "actual_goaldiff": elements[9]
        }

    for key, value in data["ITA"]["18"].items():
        for key2, value2 in value.items():
            out = ""
            for key3, value3 in value2.items():
                out += value3 + ";"
            print(out[:-1])

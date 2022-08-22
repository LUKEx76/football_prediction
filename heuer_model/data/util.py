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
with open("eff_chances.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        elements = line.split(";")

        if line.startswith("country"):
            # print(elements[0]+";"+elements[1]+";"+elements[2]+";" +
            #       elements[3]+";"+elements[4]+";"+elements[5]+";"+elements[6]+";"+elements[7]+";is_promoter;"+elements[8]+";"+elements[9])
            continue

        if elements[0] not in data.keys():
            data[elements[0]] = {}
        if elements[1] not in data[elements[0]].keys():
            data[elements[0]][elements[1]] = {}
        if elements[2] not in data[elements[0]][elements[1]].keys():
            data[elements[0]][elements[1]][elements[2]] = {}
        if elements[3] not in data[elements[0]][elements[1]][elements[2]].keys():
            data[elements[0]][elements[1]][elements[2]][elements[3]] = {
                "chances": 0, "chances_against": 0}
        if elements[4] not in data[elements[0]][elements[1]][elements[2]].keys():
            data[elements[0]][elements[1]][elements[2]][elements[4]] = {
                "chances": 0, "chances_against": 0}

        home_chances = float(elements[5])
        away_chances = float(elements[6])

        if elements[2] == "1":
            data[elements[0]][elements[1]][elements[2]][elements[3]
                                                        ]["chances"] = home_chances
            data[elements[0]][elements[1]][elements[2]][elements[3]
                                                        ]["chances_against"] = away_chances

            data[elements[0]][elements[1]][elements[2]][elements[4]
                                                        ]["chances"] = away_chances
            data[elements[0]][elements[1]][elements[2]][elements[4]
                                                        ]["chances_against"] = home_chances
        else:
            data[elements[0]][elements[1]][elements[2]][elements[3]
                                                        ]["chances"] = data[elements[0]][elements[1]][str(int(elements[2]) - 1)][elements[3]
                                                                                                                                 ]["chances"] + home_chances
            data[elements[0]][elements[1]][elements[2]][elements[3]
                                                        ]["chances_against"] = data[elements[0]][elements[1]][str(int(elements[2]) - 1)][elements[3]
                                                                                                                                         ]["chances_against"] + away_chances

            data[elements[0]][elements[1]][elements[2]][elements[4]
                                                        ]["chances"] = data[elements[0]][elements[1]][str(int(elements[2]) - 1)][elements[4]
                                                                                                                                 ]["chances"] + away_chances
            data[elements[0]][elements[1]][elements[2]][elements[4]
                                                        ]["chances_against"] = data[elements[0]][elements[1]][str(int(elements[2]) - 1)][elements[4]
                                                                                                                                         ]["chances_against"] + home_chances

with open("matches.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        elements = line.split(";")

        if line.startswith("country"):
            print(elements[0]+";"+elements[1]+";"+elements[2]+";" +
                  elements[3]+";curr_eff_chancediff;"+elements[5]+";"+elements[6]+";"+elements[7]+";" + elements[8] + ";"+elements[9]+";"+elements[10])
            continue

        curr_eff_chancediff = 0

        if int(elements[2]) > 1:
            if elements[0] == "GER":
                curr_eff_chancediff = (1 + 0.024 * float(elements[5])) * float(data[elements[0]][elements[1]][str(int(elements[2]) - 1)][elements[3]]["chances"]) * 34 - (
                    1 - 0.024 * float(elements[5])) * float(data[elements[0]][elements[1]][str(int(elements[2]) - 1)][elements[3]]["chances_against"]) * 34
            else:

                curr_eff_chancediff = (1 + 0.024 * float(elements[5])) * float(data[elements[0]][elements[1]][str(int(elements[2]) - 1)][elements[3]]["chances"]) * 38 - (
                    1 - 0.024 * float(elements[5])) * float(data[elements[0]][elements[1]][str(int(elements[2]) - 1)][elements[3]]["chances_against"]) * 38

            curr_eff_chancediff = curr_eff_chancediff / (int(elements[2]) - 1)

        print(elements[0]+";"+elements[1]+";"+elements[2]+";" +
              elements[3]+";"+str(curr_eff_chancediff) + ";"+elements[5]+";"+elements[6]+";"+elements[7]+";" +
              elements[8] + ";" + elements[9]+";" + elements[10])

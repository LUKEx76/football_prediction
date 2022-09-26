import numpy as np

season_data = dict()

with open("season_hf_adv.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            continue

        items = line.split(";")

        if items[0] not in season_data.keys():
            season_data[items[0]] = {}
        if items[1] not in season_data[items[0]].keys():
            season_data[items[0]][items[1]] = {}

        season_data[items[0]][items[1]] = float(items[2])


curr_data = dict()

with open("curr_hf_adv.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            continue

        items = line.split(";")

        if items[0] not in curr_data.keys():
            curr_data[items[0]] = {}
        if items[1] not in curr_data[items[0]].keys():
            curr_data[items[0]][items[1]] = {}
        if items[2] not in curr_data[items[0]][items[1]].keys():
            curr_data[items[0]][items[1]][items[2]] = {}

        if str(int(items[2])-1) in curr_data[items[0]][items[1]].keys():
            curr_data[items[0]][items[1]][items[2]]["count"] = curr_data[items[0]
                                                                         ][items[1]][str(int(items[2])-1)]["count"] + 1
            curr_data[items[0]][items[1]][items[2]]["sum"] = curr_data[items[0]
                                                                       ][items[1]][str(int(items[2])-1)]["sum"] + float(items[3])
        else:
            curr_data[items[0]][items[1]][items[2]]["count"] = 1
            curr_data[items[0]][items[1]][items[2]]["sum"] = float(items[3])


with open("frame.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            print(
                "country;season;matchnumber;ht_name;at_name;curr_hf_adv;past_hf_adv;actual_hf_adv")
            continue

        items = line.split(";")

        curr_hf_adv, past_hf_adv = 0, 0
        if str(int(items[2])-1) in curr_data[items[0]][items[1]].keys():
            curr_hf_adv = curr_data[items[0]][items[1]
                                              ][str(int(items[2])-1)]["sum"] / curr_data[items[0]][items[1]
                                                                                                   ][str(int(items[2])-1)]["count"]

        if items[2] == "14":
            past_hf_adv = 0
        if items[2] == "15":
            past_hf_adv = season_data[items[0]]["14"]
        if items[2] == "16":
            past_hf_adv = (season_data[items[0]
                                       ]["14"] + season_data[items[0]]["15"]) / 2
        if items[2] == "17":
            past_hf_adv = (season_data[items[0]
                                       ]["14"] + season_data[items[0]]["15"] + season_data[items[0]]["16"]) / 3
        if items[2] == "18":
            past_hf_adv = (season_data[items[0]
                                       ]["15"] + season_data[items[0]]["16"] + season_data[items[0]]["17"]) / 3

        print(items[0] + ";"+items[1] + ";"+items[2]+";"+items[3] +
              ";"+items[4]+";"+str(curr_hf_adv)+";"+str(past_hf_adv)+";"+items[5])

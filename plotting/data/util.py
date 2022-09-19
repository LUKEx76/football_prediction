

data = dict()
with open("chances.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            continue

        items = line.split(";")

        if items[0] not in data.keys():
            data[items[0]] = {}
        if items[1] not in data[items[0]].keys():
            data[items[0]][items[1]] = {}
        if items[2] not in data[items[0]][items[1]].keys():
            data[items[0]][items[1]][items[2]] = {}
        if items[3] not in data[items[0]][items[1]][items[2]].keys():
            data[items[0]][items[1]][items[2]][items[3]] = {
                "chances": 0, "chances_against": 0}
        if items[4] not in data[items[0]][items[1]][items[2]].keys():
            data[items[0]][items[1]][items[2]][items[4]] = {
                "chances": 0, "chances_against": 0}

        if int(items[2]) > 1:
            data[items[0]][items[1]][items[2]][items[3]]["chances"] = data[items[0]
                                                                           ][items[1]][str(int(items[2])-1)][items[3]]["chances"] + int(items[5])
            data[items[0]][items[1]][items[2]][items[3]]["chances_against"] = data[items[0]
                                                                                   ][items[1]][str(int(items[2])-1)][items[3]]["chances_against"] + int(items[6])
            data[items[0]][items[1]][items[2]][items[4]]["chances"] = data[items[0]
                                                                           ][items[1]][str(int(items[2])-1)][items[4]]["chances"] + int(items[6])
            data[items[0]][items[1]][items[2]][items[4]]["chances_against"] = data[items[0]
                                                                                   ][items[1]][str(int(items[2])-1)][items[4]]["chances_against"] + int(items[5])
        else:
            data[items[0]][items[1]][items[2]
                                     ][items[3]]["chances"] = int(items[5])
            data[items[0]][items[1]][items[2]][items[3]
                                               ]["chances_against"] = int(items[6])
            data[items[0]][items[1]][items[2]
                                     ][items[4]]["chances"] = int(items[6])
            data[items[0]][items[1]][items[2]][items[4]
                                               ]["chances_against"] = int(items[5])


with open("plot_matches.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            print(
                line+";ht_curr_chancediff;at_curr_chancediff;ht_curr_chanceamount;at_curr_chanceamount")
            continue

        items = line.split(";")

        ht_curr_chancediff, at_curr_chancediff = 0, 0
        ht_curr_chanceamount, at_curr_chanceamount = 0, 0

        if int(items[2]) > 1:
            ht_curr_chancediff = (float(data[items[0]][items[1]][str(int(
                items[2])-1)][items[3]]["chances"]) - float(data[items[0]][items[1]][str(int(items[2])-1)][items[3]]["chances_against"])) / (int(items[2])-1)
            at_curr_chancediff = (float(data[items[0]][items[1]][str(int(
                items[2])-1)][items[4]]["chances"]) - float(data[items[0]][items[1]][str(int(items[2])-1)][items[4]]["chances_against"])) / (int(items[2])-1)
            ht_curr_chanceamount = float(data[items[0]][items[1]][str(
                int(items[2])-1)][items[3]]["chances"]) / (int(items[2])-1)
            at_curr_chanceamount = float(data[items[0]][items[1]][str(
                int(items[2])-1)][items[4]]["chances"]) / (int(items[2])-1)

        print(line+";"+str(ht_curr_chancediff)+";"+str(at_curr_chancediff) +
              ";"+str(ht_curr_chanceamount)+";"+str(at_curr_chanceamount))


avg_ga_data = dict()

with open("avg_xga.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            continue

        items = line.split(";")

        if items[0] not in avg_ga_data.keys():
            avg_ga_data[items[0]] = {}
        if items[1] not in avg_ga_data[items[0]].keys():
            avg_ga_data[items[0]][items[1]] = {}
        if items[2] not in avg_ga_data[items[0]][items[1]].keys():
            avg_ga_data[items[0]][items[1]][items[2]] = {
                "amount": 0, "count": 0}

        if items[2] == "1":
            avg_ga_data[items[0]][items[1]][items[2]
                                            ]["amount"] = float(items[3])
            avg_ga_data[items[0]][items[1]][items[2]
                                            ]["count"] = 1
        else:
            avg_ga_data[items[0]][items[1]][items[2]]["amount"] = avg_ga_data[items[0]][items[1]][str(
                int(items[2])-1)]["amount"] + float(items[3])
            avg_ga_data[items[0]][items[1]][items[2]]["count"] = avg_ga_data[items[0]][items[1]][str(
                int(items[2])-1)]["count"] + 1


data = dict()
with open("plot_matches.csv", "r") as file:
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
                "curr_xg_diff": 0, "curr_xg_amount": 0}
        if items[4] not in data[items[0]][items[1]][items[2]].keys():
            data[items[0]][items[1]][items[2]][items[4]] = {
                "curr_xg_diff": 0, "curr_xg_amount": 0}

        data[items[0]][items[1]][items[2]][items[3]
                                           ]["curr_xg_diff"] = float(items[31])
        data[items[0]][items[1]][items[2]][items[3]
                                           ]["curr_xg_amount"] = float(items[35])

        data[items[0]][items[1]][items[2]][items[4]
                                           ]["curr_xg_diff"] = float(items[32])
        data[items[0]][items[1]][items[2]][items[4]
                                           ]["curr_xg_amount"] = float(items[36])


with open("plot_matches.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            print(line)
            # country;season;matchnumber;ht_name;at_name;
            # ht_curr_eff_chancediff;at_curr_eff_chancediff;ht_last_year_chancediff;at_last_year_chancediff;
            # ht_past_chancediff_combined;at_past_chancediff_combined;ht_curr_eff_chanceamount;at_curr_eff_chanceamount;
            # ht_past_chanceamount;at_past_chanceamount;ht_fitness;at_fitness;
            # ht_market_value_ln_relative;at_market_value_ln_relative;ht_is_promoter;at_is_promoter;
            # xg_amount;xg_diff;actual_goalamount;actual_goaldiff;
            # ht_market_value;at_market_value;ht_market_value_ln;at_market_value_ln;
            # ht_curr_chancediff;at_curr_chancediff;ht_curr_chanceamount;at_curr_chanceamount;
            # ht_last_year_chanceamount;at_last_year_chanceamount"
            # print("country;season;matchnumber;ht_name;at_name;" +
            #       "ht_curr_eff_chancediff;at_curr_eff_chancediff;ht_past_chancediff_combined;at_past_chancediff_combined;" +
            #       "ht_curr_eff_chanceamount;at_curr_eff_chanceamount;ht_past_chanceamount;at_past_chanceamount;" +
            #       "ht_fitness;at_fitness;ht_market_value_ln_relative;at_market_value_ln_relative;ht_is_promoter;at_is_promoter;" +
            #       "ht_curr_chancediff;at_curr_chancediff;ht_last_year_chancediff;at_last_year_chancediff;" +
            #       "ht_curr_chanceamount;at_curr_chanceamount;ht_last_year_chanceamount;at_last_year_chanceamount;" +
            #       "ht_market_value;at_market_value;ht_market_value_ln;at_market_value_ln;" +
            #       "ht_curr_xg_diff;at_curr_xg_diff;ht_last_year_xg_diff;at_last_year_xg_diff;" +
            #       "ht_curr_xg_amount;at_curr_xg_amount;ht_last_year_xg_amount;at_last_year_xg_amount;" +
            #       "xg_amount;xg_diff;actual_goalamount;actual_goaldiff")
            continue

        items = line.split(";")

        ht_curr_xg_diff, at_curr_xg_diff = 0, 0
        ht_curr_xg_amount, at_curr_xg_amount = 0, 0

        if items[2] != "1":
            ht_curr_xg_diff = data[items[0]][items[1]
                                             ][str(int(items[2])-1)][items[3]]["curr_xg_diff"]
            at_curr_xg_diff = data[items[0]][items[1]
                                             ][str(int(items[2])-1)][items[4]]["curr_xg_diff"]

            ht_curr_xg_amount = data[items[0]][items[1]
                                               ][str(int(items[2])-1)][items[3]]["curr_xg_amount"] - (avg_ga_data[items[0]][items[1]][str(int(items[2])-1)]["amount"] / avg_ga_data[items[0]][items[1]][str(int(items[2])-1)]["count"])
            at_curr_xg_amount = data[items[0]][items[1]
                                               ][str(int(items[2])-1)][items[4]]["curr_xg_amount"] - (avg_ga_data[items[0]][items[1]][str(int(items[2])-1)]["amount"] / avg_ga_data[items[0]][items[1]][str(int(items[2])-1)]["count"])

        out = ""
        for item in items[0:31]:
            out += item + ";"

        out += str(ht_curr_xg_diff) + ";" + str(at_curr_xg_diff) + ";" + items[33] + ";" + items[34] + ";" + \
            str(ht_curr_xg_amount) + ";" + str(at_curr_xg_amount) + ";" + \
            items[37] + ";" + items[38] + ";" + \
            items[39] + ";" + items[40] + ";" + items[41] + ";" + items[42]

        print(out)

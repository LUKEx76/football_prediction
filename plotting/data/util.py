rel = dict()

with open("rel.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            continue

        items = line.split(";")

        if items[0] not in rel.keys():
            rel[items[0]] = {}
        if items[1] not in rel[items[0]].keys():
            rel[items[0]][items[1]] = {"rel_sum": 0, "rel_diff": 0}

        rel[items[0]][items[1]]["rel_diff"] = float(items[2])
        rel[items[0]][items[1]]["rel_sum"] = float(items[3])


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
            data[items[0]][items[1]][items[2]] = {
                "chance_diff": 0, "chance_sum": 0}

        data[items[0]][items[1]][items[2]]["chance_diff"] = float(items[4])
        data[items[0]][items[1]][items[2]]["chance_sum"] = float(items[3])


with open("plot_matches.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            # country;season;matchnumber;ht_name;at_name;
            # ht_curr_eff_chancediff;at_curr_eff_chancediff;ht_last_year_chancediff;at_last_year_chancediff;
            # ht_past_chancediff_combined;at_past_chancediff_combined;ht_curr_eff_chanceamount;at_curr_eff_chanceamount;
            # ht_past_chanceamount;at_past_chanceamount;ht_fitness;at_fitness;
            # ht_market_value_ln_relative;at_market_value_ln_relative;ht_is_promoter;at_is_promoter;
            # xg_amount;xg_diff;actual_goalamount;actual_goaldiff;
            # ht_market_value;at_market_value;ht_market_value_ln;at_market_value_ln;
            # ht_curr_chancediff;at_curr_chancediff;ht_curr_chanceamount;at_curr_chanceamount;
            # ht_last_year_chanceamount;at_last_year_chanceamount"
            print("country;season;matchnumber;ht_name;at_name;" +
                  "ht_curr_eff_chancediff;at_curr_eff_chancediff;ht_past_chancediff_combined;at_past_chancediff_combined;" +
                  "ht_curr_eff_chanceamount;at_curr_eff_chanceamount;ht_past_chanceamount;at_past_chanceamount;" +
                  "ht_fitness;at_fitness;ht_market_value_ln_relative;at_market_value_ln_relative;ht_is_promoter;at_is_promoter;" +
                  "ht_curr_chancediff;at_curr_chancediff;ht_last_year_chancediff;at_last_year_chancediff;" +
                  "ht_curr_chanceamount;at_curr_chanceamount;ht_last_year_chanceamount;at_last_year_chanceamount;" +
                  "ht_market_value;at_market_value;ht_market_value_ln;at_market_value_ln;" +
                  "xg_amount;xg_diff;actual_goalamount;actual_goaldiff")
            continue

        items = line.split(";")

        ht_ly_chancediff, at_ly_chancediff = 0, 0
        ht_ly_chanceamount, at_ly_chanceamount = 0, 0

        if int(items[1]) > 14:
            if items[3] in data[items[0]][str(int(items[1])-1)].keys():
                ht_ly_chanceamount = data[items[0]
                                          ][str(int(items[1])-1)][items[3]]["chance_sum"]
                ht_ly_chancediff = data[items[0]
                                        ][str(int(items[1])-1)][items[3]]["chance_diff"]
            else:
                ht_ly_chanceamount = rel[items[0]][str(
                    int(items[1])-1)]["rel_sum"]
                ht_ly_chancediff = rel[items[0]
                                       ][str(int(items[1])-1)]["rel_diff"]

            if items[4] in data[items[0]][str(int(items[1])-1)].keys():
                at_ly_chanceamount = data[items[0]
                                          ][str(int(items[1])-1)][items[4]]["chance_sum"]
                at_ly_chancediff = data[items[0]
                                        ][str(int(items[1])-1)][items[4]]["chance_diff"]
            else:
                at_ly_chanceamount = rel[items[0]][str(
                    int(items[1])-1)]["rel_sum"]
                at_ly_chancediff = rel[items[0]
                                       ][str(int(items[1])-1)]["rel_diff"]

        print(
            items[0] + ";" + items[1] + ";" + items[2] + ";" + items[3] + ";" + items[4] + ";" + items[5] + ";" + items[6] + ";" +
            items[9] + ";" + items[10] + ";" + items[11] + ";" + items[12] + ";" + items[13] + ";" + items[14] + ";" + items[15] + ";" +
            items[16] + ";" + items[17] + ";" + items[18] + ";" + items[19] + ";" + items[20] + ";" + items[29] + ";" + items[30] + ";" +
            str(ht_ly_chancediff) + ";" + str(at_ly_chancediff) + ";" + items[31] + ";" + items[32] + ";" + str(ht_ly_chanceamount) + ";" + str(at_ly_chanceamount) + ";" + items[25] + ";" +
            items[26] + ";" + items[27] + ";" + items[28] + ";" +
            items[21] + ";" + items[22] + ";" + items[23] + ";" + items[24]
        )

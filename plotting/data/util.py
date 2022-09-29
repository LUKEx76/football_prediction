
ann_rel = dict()

with open("rel.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            continue

        items = line.split(";")

        if items[0] not in ann_rel.keys():
            ann_rel[items[0]] = {}
        if items[1] not in ann_rel[items[0]].keys():
            ann_rel[items[0]][items[1]] = {"rel_diff": 0, "rel_amount": 0}

        ann_rel[items[0]][items[1]]["rel_diff"] = float(items[2])
        ann_rel[items[0]][items[1]]["rel_amount"] = float(items[3])


ann = dict()
with open("annual.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            continue

        items = line.split(";")

        if items[0] not in ann.keys():
            ann[items[0]] = {}
        if items[1] not in ann[items[0]].keys():
            ann[items[0]][items[1]] = {}
        if items[2] not in ann[items[0]].keys():
            ann[items[0]][items[1]][items[2]] = {
                "ann_diff": 0, "ann_amount": 0}

        ann[items[0]][items[1]][items[2]]["ann_diff"] = float(items[3])
        ann[items[0]][items[1]][items[2]]["ann_amount"] = float(items[4])


curr = dict()
with open("curr.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            continue

        items = line.split(";")

        if items[0] not in curr.keys():
            curr[items[0]] = {}
        if items[1] not in curr[items[0]].keys():
            curr[items[0]][items[1]] = {}
        if items[2] not in curr[items[0]][items[1]].keys():
            curr[items[0]][items[1]][items[2]] = {}
        if items[3] not in curr[items[0]][items[1]][items[2]].keys():
            curr[items[0]][items[1]][items[2]][items[3]] = {
                "curr_diff": 0, "curr_amount": 0, "count": 0}
        if items[4] not in curr[items[0]][items[1]][items[2]].keys():
            curr[items[0]][items[1]][items[2]][items[4]] = {
                "curr_diff": 0, "curr_amount": 0, "count": 0}

        if items[2] == "1":
             # home
            curr[items[0]][items[1]][items[2]][items[3]
                                               ]["curr_diff"] = float(items[5]) - float(items[6])
            curr[items[0]][items[1]][items[2]][items[3]
                                               ]["curr_amount"] = float(items[5])
            curr[items[0]][items[1]][items[2]][items[3]
                                               ]["count"] = 1
            # away
            curr[items[0]][items[1]][items[2]][items[4]
                                               ]["curr_diff"] = float(items[6]) - float(items[5])
            curr[items[0]][items[1]][items[2]][items[4]
                                               ]["curr_amount"] = float(items[6])
            curr[items[0]][items[1]][items[2]][items[4]
                                               ]["count"] = 1
        else:
            # home
            curr[items[0]][items[1]][items[2]][items[3]
                                               ]["curr_diff"] = curr[items[0]][items[1]][str(int(items[2])-1)][items[3]
                                                                                                               ]["curr_diff"] + float(items[5]) - float(items[6])
            curr[items[0]][items[1]][items[2]][items[3]
                                               ]["curr_amount"] = curr[items[0]][items[1]][str(int(items[2])-1)][items[3]
                                                                                                                 ]["curr_amount"] + float(items[5])
            curr[items[0]][items[1]][items[2]][items[3]
                                               ]["count"] = curr[items[0]][items[1]][str(int(items[2])-1)][items[3]
                                                                                                           ]["count"] + 1
            # away
            curr[items[0]][items[1]][items[2]][items[4]
                                               ]["curr_diff"] = curr[items[0]][items[1]][str(int(items[2])-1)][items[4]
                                                                                                               ]["curr_diff"] + float(items[6]) - float(items[5])
            curr[items[0]][items[1]][items[2]][items[4]
                                               ]["curr_amount"] = curr[items[0]][items[1]][str(int(items[2])-1)][items[4]
                                                                                                                 ]["curr_amount"] + float(items[6])
            curr[items[0]][items[1]][items[2]][items[4]
                                               ]["count"] = curr[items[0]][items[1]][str(int(items[2])-1)][items[4]
                                                                                                           ]["count"] + 1


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
                  "ht_curr_xg_diff;at_curr_xg_diff;ht_last_year_xg_diff;at_last_year_xg_diff;" +
                  "ht_curr_xg_amount;at_curr_xg_amount;ht_last_year_xg_amount;at_last_year_xg_amount;" +
                  "xg_amount;xg_diff;actual_goalamount;actual_goaldiff")
            continue

        items = line.split(";")

        ht_curr_xg_diff, at_curr_xg_diff = 0, 0
        ht_ly_xg_diff, at_ly_xg_diff = 0, 0

        ht_curr_xg_amount, at_curr_xg_amount = 0, 0
        ht_ly_xg_amount, at_ly_xg_amount = 0, 0

        ht_curr_xg_diff = curr[items[0]][items[1]][items[2]][items[3]
                                                             ]["curr_diff"] / curr[items[0]][items[1]][items[2]][items[3]]["count"]
        at_curr_xg_diff = curr[items[0]][items[1]][items[2]][items[4]
                                                             ]["curr_diff"] / curr[items[0]][items[1]][items[2]][items[4]]["count"]

        ht_curr_xg_amount = curr[items[0]][items[1]][items[2]][items[3]
                                                               ]["curr_amount"] / curr[items[0]][items[1]][items[2]][items[3]]["count"]
        at_curr_xg_amount = curr[items[0]][items[1]][items[2]][items[4]
                                                               ]["curr_amount"] / curr[items[0]][items[1]][items[2]][items[4]]["count"]

        if items[1] != "14":
            if items[3] in ann[items[0]][items[1]].keys():
                ht_ly_xg_diff = ann[items[0]
                                    ][items[1]][items[3]]["ann_diff"]
                ht_ly_xg_amount = ann[items[0]
                                      ][items[1]][items[3]]["ann_amount"]
            else:
                ht_ly_xg_diff = ann_rel[items[0]][items[1]]["rel_diff"]
                ht_ly_xg_amount = ann_rel[items[0]][items[1]]["rel_amount"]
            if items[4] in ann[items[0]][items[1]].keys():
                at_ly_xg_diff = ann[items[0]
                                    ][items[1]][items[4]]["ann_diff"]
                at_ly_xg_amount = ann[items[0]
                                      ][items[1]][items[4]]["ann_amount"]
            else:
                at_ly_xg_diff = ann_rel[items[0]][items[1]]["rel_diff"]
                at_ly_xg_amount = ann_rel[items[0]][items[1]]["rel_amount"]

        out = ""
        for item in items[0:31]:
            out += item + ";"

        out += str(ht_curr_xg_diff) + ";" + str(at_curr_xg_diff) + ";" + str(ht_ly_xg_diff) + ";" + str(at_ly_xg_diff) + ";" + \
            str(ht_curr_xg_amount) + ";" + str(at_curr_xg_amount) + ";" + \
            str(ht_ly_xg_amount) + ";" + str(at_ly_xg_amount) + ";" + \
            items[31] + ";" + items[32] + ";" + items[33] + ";" + items[34]

        print(out)

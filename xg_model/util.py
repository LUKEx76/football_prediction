data = dict()

with open("ga.csv", "r") as xg_file:
    for line in xg_file:
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
            data[elements[0]][elements[1]][elements[2]
                                           ][elements[3]] = {"actual_goalamount": elements[17], "actual_goaldiff": elements[18]}


with open("matches_xg.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            print("country;season;matchnumber;ht_name;at_name;ht_curr_eff_chancediff;at_curr_eff_chancediff;ht_past_chancediff_combined;at_past_chancediff_combined;ht_curr_eff_chanceamount;at_curr_eff_chanceamount;ht_past_chanceamount;at_past_chanceamount;ht_market_value_ln_relative;at_market_value_ln_relative;ht_is_promoter;at_is_promoter;xg_amount;xg_diff;actual_goalamount;actual_goaldiff")
            continue

        elements = line.split(";")

        print(elements[0] + ";" + elements[1] + ";" +
              elements[2] + ";" + elements[3] + ";" +
              elements[4] + ";" + elements[5] + ";" +
              elements[6] + ";" + elements[7] + ";" +
              elements[8] + ";" + elements[9] + ";" +
              elements[10] + ";" + elements[11] + ";" +
              elements[12] + ";" + elements[13] + ";" +
              elements[14] + ";" + elements[15] + ";" +
              elements[16] + ";" + elements[17] + ";" + elements[18] + ";" +
              data[elements[0]][elements[1]][elements[2]][elements[3]]["actual_goalamount"] + ";" +
              data[elements[0]][elements[1]][elements[2]][elements[3]]["actual_goaldiff"])

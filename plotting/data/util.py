
rel_data = dict()

with open("rel.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            continue

        items = line.split(";")

        if items[0] not in rel_data.keys():
            rel_data[items[0]] = {}
        if items[1] not in rel_data[items[0]].keys():
            rel_data[items[0]][items[1]] = {}

        rel_data[items[0]][items[1]] = float(items[2].strip())

data = dict()
with open("past_chancediff.csv", "r") as file:
    for line in file:
        if line.startswith("country"):
            continue

        line = line.replace("\n", "")
        items = line.split(";")

        if items[0] not in data.keys():
            data[items[0]] = {}
        if items[1] not in data[items[0]].keys():
            data[items[0]][items[1]] = {}
        if items[2] not in data[items[0]][items[1]].keys():
            data[items[0]][items[1]][items[2]] = {}

        data[items[0]][items[1]][items[2]] = float(items[3].strip())


with open("plot_matches.csv", "r") as file:
    for line in file:
        if line.startswith("country"):
            print("country;season;matchnumber;ht_name;at_name;ht_curr_eff_chancediff;at_curr_eff_chancediff;ht_last_year_chancediff;at_last_year_chancediff;ht_past_chancediff_combined;at_past_chancediff_combined;ht_curr_eff_chanceamount;at_curr_eff_chanceamount;ht_past_chanceamount;at_past_chanceamount;ht_fitness;at_fitness;ht_market_value_ln_relative;at_market_value_ln_relative;ht_is_promoter;at_is_promoter;xg_amount;xg_diff;actual_goalamount;actual_goaldiff")
            continue

        line = line.replace("\n", "")
        items = line.split(";")

        ht_last_year_chancediff = 0
        at_last_year_chancediff = 0

        if not items[1] == "14":
            if items[3] in data[items[0]][str(int(items[1])-1)].keys():
                ht_last_year_chancediff = data[items[0]][str(
                    int(items[1])-1)][items[3]]
            else:
                ht_last_year_chancediff = float(rel_data[items[0]][str(
                    int(items[1])-1)])
            if items[4] in data[items[0]][str(int(items[1])-1)].keys():
                at_last_year_chancediff = float(data[items[0]][str(
                    int(items[1])-1)][items[4]])
            else:
                at_last_year_chancediff = float(rel_data[items[0]][str(
                    int(items[1])-1)])

        print(items[0] + ";" + items[1] + ";" + items[2] + ";" + items[3] + ";" + items[4] + ";" + items[5] + ";" +
              items[6] + ";" + str(ht_last_year_chancediff) + ";" + str(at_last_year_chancediff) + ";" + items[7] + ";" +
              items[8] + ";" + items[9] + ";" + items[10].strip() + ";" + items[11].strip() + ";" + items[12] + ";" + items[13] + ";" +
              items[14] + ";" + items[15] + ";" + items[16] + ";" + items[17] + ";" + items[18] + ";" + items[19] + ";" +
              items[20] + ";" + items[21] + ";" + items[22])

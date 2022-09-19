import numpy as np

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
            data[items[0]][items[1]][items[2]][items[3]] = {}
        if items[4] not in data[items[0]][items[1]][items[2]].keys():
            data[items[0]][items[1]][items[2]][items[4]] = {}

        data[items[0]][items[1]][items[2]][items[3]] = int(
            items[5]) - int(items[6])
        data[items[0]][items[1]][items[2]][items[4]] = int(
            items[6]) - int(items[5])


with open("matches_xg.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            print("country;season;matchnumber;ht_name;at_name;ht_curr_eff_chancediff;at_curr_eff_chancediff;ht_past_chancediff_combined;at_past_chancediff_combined;ht_curr_eff_chanceamount;at_curr_eff_chanceamount;ht_past_chanceamount;at_past_chanceamount;ht_fitness;at_fitness;ht_market_value_ln_relative;at_market_value_ln_relative;ht_is_promoter;at_is_promoter;xg_amount;xg_diff;actual_goalamount;actual_goaldiff")
            continue

        items = line.split(";")

        fac = 0.655
        ht_fitness, at_fitness = 0, 0

        if str(int(items[2])-1) in data[items[0]][items[1]].keys():
            ht_fitness += data[items[0]][items[1]
                                         ][str(int(items[2])-1)][items[3]] * np.exp(-1*fac)
        if str(int(items[2])-2) in data[items[0]][items[1]].keys():
            ht_fitness += data[items[0]][items[1]
                                         ][str(int(items[2])-2)][items[3]] * np.exp(-2*fac)
        if str(int(items[2])-3) in data[items[0]][items[1]].keys():
            ht_fitness += data[items[0]][items[1]
                                         ][str(int(items[2])-3)][items[3]] * np.exp(-3*fac)
        if str(int(items[2])-4) in data[items[0]][items[1]].keys():
            ht_fitness += data[items[0]][items[1]
                                         ][str(int(items[2])-4)][items[3]] * np.exp(-4*fac)

        if str(int(items[2])-1) in data[items[0]][items[1]].keys():
            at_fitness += data[items[0]][items[1]
                                         ][str(int(items[2])-1)][items[4]] * np.exp(-1*fac)
        if str(int(items[2])-2) in data[items[0]][items[1]].keys():
            at_fitness += data[items[0]][items[1]
                                         ][str(int(items[2])-2)][items[4]] * np.exp(-2*fac)
        if str(int(items[2])-3) in data[items[0]][items[1]].keys():
            at_fitness += data[items[0]][items[1]
                                         ][str(int(items[2])-3)][items[4]] * np.exp(-3*fac)
        if str(int(items[2])-4) in data[items[0]][items[1]].keys():
            at_fitness += data[items[0]][items[1]
                                         ][str(int(items[2])-4)][items[4]] * np.exp(-4*fac)

        print(items[0] + ";" + items[1] + ";" + items[2] + ";" + items[3] + ";" + items[4] + ";" + items[5] + ";" +
              items[6] + ";" + items[7] + ";" + items[8] + ";" + items[9] + ";" + items[10] + "; " +
              items[11] + ";" + items[12] + ";" + str(ht_fitness) + ";" + str(at_fitness) + ";" +
              items[13] + ";" + items[14] + ";" + items[15] + ";" + items[16] + ";" + items[17] + ";" + items[18] + ";" + items[19] + ";" + items[20])

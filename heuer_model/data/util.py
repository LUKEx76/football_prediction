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


with open("matches_heuer.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            print("country;season;matchnumber;teamname;curr_eff_chancediff;past_chancediff_combined;curr_eff_chanceamount;past_chanceamount;curr_fitness;market_value_ln_relative;is_promoter;is_home;actual_goalamount;actual_goaldiff")
            continue

        items = line.split(";")

        fac = 0.655
        fitness = 0

        if str(int(items[2])-1) in data[items[0]][items[1]].keys():
            fitness += data[items[0]][items[1]
                                      ][str(int(items[2])-1)][items[3]] * np.exp(-1*fac)
        if str(int(items[2])-2) in data[items[0]][items[1]].keys():
            fitness += data[items[0]][items[1]
                                      ][str(int(items[2])-2)][items[3]] * np.exp(-2*fac)
        if str(int(items[2])-3) in data[items[0]][items[1]].keys():
            fitness += data[items[0]][items[1]
                                      ][str(int(items[2])-3)][items[3]] * np.exp(-3*fac)
        if str(int(items[2])-4) in data[items[0]][items[1]].keys():
            fitness += data[items[0]][items[1]
                                      ][str(int(items[2])-4)][items[3]] * np.exp(-4*fac)

        print(items[0] + ";" + items[1] + ";" + items[2] + ";" + items[3] + ";" + items[4] + ";" + items[5] + ";" +
              items[6] + ";" + items[7] + ";" + str(fitness) + ";" + items[8] + ";" + items[9] + ";" + items[10] + "; " +
              items[11] + ";" + items[12])

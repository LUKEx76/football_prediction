
with open("teamstrength.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            print(
                "country;season;matchnumber;teamname;curr_chance_diff;past_chance_diff1;past_chance_diff2;past_chance_diff3;marketvalue")
            continue

        elements = line.split(";")

        base = elements[0] + ";" + elements[1] + ";" + elements[2] + ";"
        hometeam = base + elements[3] + ";" + \
            str(elements[5]) + ";" + str(elements[7]) + ";" + str(elements[9]
                                                                  ) + ";" + str(elements[11]) + ";" + str(elements[13])

        awayteam = base + elements[4] + ";" + \
            str(elements[6]) + ";" + str(elements[8]) + ";" + str(elements[10]
                                                                  ) + ";" + str(elements[12]) + ";" + str(elements[14])

        print(hometeam)
        print(awayteam)

        # if elements[0] not in data.keys():
        #     data[elements[0]] = {}
        # if elements[1] not in data[elements[0]].keys():
        #     data[elements[0]][elements[1]] = {}
        # # hometeam
        # if elements[3] not in data[elements[0]][elements[1]].keys():
        #     data[elements[0]][elements[1]][elements[3]] = {}
        # # awayteam
        # if elements[4] not in data[elements[0]][elements[1]].keys():
        #     data[elements[0]][elements[1]][elements[4]] = {}

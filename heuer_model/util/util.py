import copy

with open("country_season_goalamount.csv", "r") as file:
    last_country = ""
    prev_current_season_goalamount = 0
    counter = 0
    for line in file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            print(line)
            continue

        elements = line.split(";")

        if elements[0] == last_country:
            tmp = copy.copy(elements[4])
            elements[4] = prev_current_season_goalamount
            prev_current_season_goalamount = tmp
        else:
            prev_current_season_goalamount = elements[4]
            elements[4] = 0

        last_country = elements[0]
        out = ""
        for element in elements:
            out += str(element) + ";"

        print(out[:-1])

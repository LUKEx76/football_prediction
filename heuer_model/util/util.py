
with open("country_season_homefield_adv.csv", "r") as file:
    data = dict()
    for line in file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            print(line + ";hf_adv_current_season")
            continue

        elements = line.split(";")

        if elements[0] not in data.keys():
            data[elements[0]] = {}

        if elements[1] not in data[elements[0]].keys():
            data[elements[0]][elements[1]] = {
                "total": 0, "count": 0, "mean": 0}

        data[elements[0]][elements[1]]["total"] += float(elements[3])
        data[elements[0]][elements[1]]["count"] += 1
        data[elements[0]][elements[1]
                          ]["mean"] = float(data[elements[0]][elements[1]]["total"] / data[elements[0]][elements[1]]["count"])

        # out = ""
        # for element in elements:
        #     out += str(element) + ";"

        print(line+";"+str(data[elements[0]][elements[1]
                                             ]["mean"]))

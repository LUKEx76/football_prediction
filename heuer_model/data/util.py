# mean_data = dict()
# with open("chance_mean.csv", "r") as file:
#     for line in file:
#         line = line.replace("\n", "")

#         if line.startswith("country"):
#             # print(line + ";market_value_ln_relative")
#             continue

#         elements = line.split(";")

#         if elements[0] not in mean_data.keys():
#             mean_data[elements[0]] = {}
#         if elements[1] not in mean_data[elements[0]].keys():
#             mean_data[elements[0]][elements[1]] = {}

#         mean_data[elements[0]][elements[1]] = elements[2]


data = dict()
with open("teamstrength.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            print(line)
            continue

        elements = line.split(";")

        if elements[2] == "1":
            elements[2] = "0"
            elements[9] = "0"
            elements[13] = "0"
            out = ""
            for element in elements:
                out += element + ";"
            print(out[:-1])

        print(line)

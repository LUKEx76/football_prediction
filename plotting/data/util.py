

data = dict()
with open("market.csv", "r") as file:
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

        data[items[0]][items[1]][items[2]]["mv"] = items[3]
        data[items[0]][items[1]][items[2]]["mv_ln"] = items[4]


with open("plot_matches.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.startswith("country"):
            print(
                line+";ht_market_value;at_market_value;ht_market_value_ln;at_market_value_ln")
            continue

        items = line.split(";")

        ht_market_value, at_market_value = 0, 0
        ht_market_value_ln, at_market_value_ln = 0, 0

        ht_market_value = data[items[0]][items[1]][items[3]]["mv"]
        at_market_value = data[items[0]][items[1]][items[4]]["mv"]
        ht_market_value_ln = data[items[0]][items[1]][items[3]]["mv_ln"]
        at_market_value_ln = data[items[0]][items[1]][items[4]]["mv_ln"]

        print(line+";"+str(ht_market_value)+";"+str(at_market_value) +
              ";"+str(ht_market_value_ln)+";"+str(at_market_value_ln))

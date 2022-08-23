
with open("matches.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        elements = line.split(";")

        if line.startswith("country"):
            print(elements[0]+";"+elements[1]+";"+elements[2]+";" +
                  elements[3]+";"+elements[4]+";"+elements[5]+";" +
                  elements[6]+";"+elements[7]+";" + elements[8] + ";" +
                  elements[9]+";"+elements[10]+";"+elements[11])
            continue

        past_chance_amount = 0
        if elements[0] == "GER":
            past_chance_amount = float(elements[7]) / 34
        else:
            past_chance_amount = float(elements[7]) / 38

        print(elements[0]+";"+elements[1]+";"+elements[2]+";" +
              elements[3]+";" + elements[4] + ";"+elements[5]+";" +
              elements[6]+";"+str(past_chance_amount)+";" +
              elements[8] + ";" + elements[9]+";" + elements[10] + ";" + elements[11])

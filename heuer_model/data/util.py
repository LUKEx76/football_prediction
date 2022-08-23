is_home = False
with open("matches.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        elements = line.split(";")

        if line.startswith("country"):
            print(elements[0]+";"+elements[1]+";"+elements[2]+";" +
                  elements[3]+";"+elements[4]+";"+elements[5]+";" +
                  elements[6]+";"+elements[7]+";" + elements[8] + ";" +
                  elements[9]+";is_home;"+elements[10]+";"+elements[11])
            continue

        is_home = not is_home

        print(elements[0]+";"+elements[1]+";"+elements[2]+";" +
              elements[3]+";" + elements[4] + ";"+elements[5]+";" +
              elements[6]+";"+elements[7]+";" +
              elements[8] + ";" + elements[9]+";"+str(is_home).lower()+";"
              + elements[10] + ";" + elements[11])

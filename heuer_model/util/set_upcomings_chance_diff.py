

with open('./teamstrength.csv', 'r') as file:
    for line in file:
        if line.startswith("country"):
            print(line, end='')
            continue
        elements = line.split(';')

        # if elements[2] == '1' and elements[5] == "NULL" and elements[6] == "NULL":
        #     line = line.replace(";NULL;NULL;", ";0;0;")

        if "NULL" in line:
            print(elements[0], elements[1],
                  elements[2], elements[3], elements[4])

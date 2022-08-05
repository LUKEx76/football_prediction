

with open('./teamstrength.csv', 'r') as file:
    for line in file:
        if line.startswith("country"):
            print(line, end='')
            continue

        line = line.replace("\n", "")
        elements = line.split(';')

        country = "ITA"
        replace_value = -2.421052632

        if elements[0] == country and elements[1] == '15-16':
            if elements[7] == "NULL":
                elements[7] = replace_value
            if elements[8] == "NULL":
                elements[8] = replace_value
        if elements[0] == country and elements[1] == '16-17':
            if elements[9] == "NULL":
                elements[9] = replace_value
            if elements[10] == "NULL":
                elements[10] = replace_value
        if elements[0] == country and elements[1] == '17-18':
            if elements[11] == "NULL":
                elements[11] = replace_value
            if elements[12] == "NULL":
                elements[12] = replace_value

        out = ""
        i = 0
        for element in elements:
            i += 1
            out += str(element)
            if i < len(elements):
                out += ";"

        print(out)

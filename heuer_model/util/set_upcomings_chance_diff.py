

with open('./teamstrength.csv', 'r') as file:
    for line in file:
        if line.startswith("country"):
            print(line, end='')
            continue

        line = line.replace("\n", "")
        elements = line.split(';')

        country = "ITA"
        replace_value = -3.728070175

        if elements[0] == country and elements[1] == '18-19':
            if elements[7] == "NULL":
                elements[7] = replace_value
            if elements[8] == "NULL":
                elements[8] = replace_value

        out = ""
        i = 0
        for element in elements:
            i += 1
            out += str(element)
            if i < len(elements):
                out += ";"

        print(out)

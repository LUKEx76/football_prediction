
filtered_lines = []

with open("scores.csv") as file:
    for line in file:
        fields = line.split("	")
        if fields[1] == "GER1" or fields[1] == "ENG1" or fields[1] == "FRA1" or fields[1] == "SPA1" or fields[1] == "ITA1":
            fields[1] = fields[1].replace("1", "")
            if fields[0] == "14-15" or fields[0] == "15-16" or fields[0] == "16-17" or fields[0] == "17-18" or fields[0] == "18-19":
                formatted_line = fields[0] + ";" + \
                    fields[1] + ";" + fields[3] + ";" + \
                    fields[4] + ";" + fields[5] + ";" + fields[6]
                filtered_lines.append(formatted_line)

out = ""
for line in filtered_lines:
    out += line + "\n"

with open("result.csv", "w") as file:
    file.write(out)

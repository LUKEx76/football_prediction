

all_lines = []
insert_lines = []

with open("result.csv") as file:
    for line in file:
        all_lines.append(line)

with open("premier_2018_2019.csv") as file:
    i = 0
    for line in file:
        if i == 0:
            i += 1
            continue
        fields = line.split(",")
        formatted_line = "18-19;ENG;" + \
            fields[2] + ";" + fields[3] + ";" + \
            fields[4] + ";" + fields[5]
        insert_lines.append(formatted_line)

i = 0
for line in all_lines:
    fields = line.split(";")
    if fields[0] == "18-19":
        if fields[1] == "ENG":
            all_lines[all_lines.index(line)] = insert_lines[i]
            i += 1

out = ""
for line in all_lines:
    out += line.replace("\n", "") + "\n"

with open("result.csv", "w") as file:
    file.write(out)

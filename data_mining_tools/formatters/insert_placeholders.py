
all_lines = []

with open("result.csv") as file:
    for line in file:
        all_lines.append(line)

for i in range(306):
    placeholer = "17-18;GER;home team;away team;0;0"
    all_lines.append(placeholer)

for i in range(380):
    placeholer = "17-18;ENG;home team;away team;0;0"
    all_lines.append(placeholer)

for i in range(380):
    placeholer = "17-18;ITA;home team;away team;0;0"
    all_lines.append(placeholer)

for i in range(380):
    placeholer = "17-18;SPA;home team;away team;0;0"
    all_lines.append(placeholer)

for i in range(380):
    placeholer = "17-18;FRA;home team;away team;0;0"
    all_lines.append(placeholer)

for i in range(306):
    placeholer = "18-19;GER;home team;away team;0;0"
    all_lines.append(placeholer)

for i in range(380):
    placeholer = "18-19;ENG;home team;away team;0;0"
    all_lines.append(placeholer)

for i in range(380):
    placeholer = "18-19;ITA;home team;away team;0;0"
    all_lines.append(placeholer)

for i in range(380):
    placeholer = "18-19;SPA;home team;away team;0;0"
    all_lines.append(placeholer)

for i in range(380):
    placeholer = "18-19;FRA;home team;away team;0;0"
    all_lines.append(placeholer)

out = ""
for line in all_lines:
    out += line.replace("\n", "") + "\n"

with open("result.csv", "w") as file:
    file.write(out)

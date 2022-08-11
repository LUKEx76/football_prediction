
with open("teamstrength.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            print(line + ";past_chancediff_combined")
            continue

        elements = line.split(";")

        past_chance_diff_combined = float(elements[5]) * \
            0.5 + float(elements[6]) * 0.35 + float(elements[7]) * 0.15

        print(line + ";" + str(past_chance_diff_combined))

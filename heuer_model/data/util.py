
total_ga, total_gd, count = 0, 0, 0
with open("tr_error.csv") as file:
    for line in file:
        if line.startswith("country"):
            continue

        line = line.replace("\n", "")

        items = line.split(";")

        if items[1] == "17" or items[1] == "18":
            if items[0] == "GER":
                total_ga += float(items[2]) * 306
                total_gd += float(items[3]) * 306
                count += 306
            else:
                total_ga += float(items[2]) * 380
                total_gd += float(items[3]) * 380
                count += 380

    print("GA", str((total_ga/count)))
    print("GD", str((total_gd/count)))

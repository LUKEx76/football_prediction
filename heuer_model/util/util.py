
import json

with open("test.json", "r") as json_file:
    completed_season_goalamount = json.load(json_file)

    countries = ["ENG", "ESP", "FRA", "GER", "ITA"]
    seasons = ["14", "15", "16", "17", "18"]

    for country in countries:
        for season in seasons:
            if "mean" not in completed_season_goalamount[country][season].keys():
                completed_season_goalamount[country][season]["mean"] = float(
                    completed_season_goalamount[country][season]["sum"] / completed_season_goalamount[country][season]["count"])


with open("country_season_goalamount.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            print(line + ";ga_last_three_seasons")
            continue

        elements = line.split(";")

        ga_last_seasons = 0

        if elements[1] == "14":
            ga_last_seasons = 0
        if elements[1] == "15":
            ga_last_seasons = float(completed_season_goalamount[elements[0]
                                                                ]["14"]["mean"])
        if elements[1] == "16":
            ga_last_seasons = float(
                completed_season_goalamount[elements[0]]["14"]["mean"] + completed_season_goalamount[elements[0]]["15"]["mean"]) / 2
        if elements[1] == "17":
            ga_last_seasons = float(
                completed_season_goalamount[elements[0]]["14"]["mean"] + completed_season_goalamount[elements[0]]["15"]["mean"] + completed_season_goalamount[elements[0]]["16"]["mean"]) / 3
        if elements[1] == "18":
            ga_last_seasons = float(
                completed_season_goalamount[elements[0]]["15"]["mean"] + completed_season_goalamount[elements[0]]["16"]["mean"] + completed_season_goalamount[elements[0]]["17"]["mean"]) / 3

        print(line + ";" + str(ga_last_seasons))

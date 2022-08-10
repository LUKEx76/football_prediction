
import json

with open("test.json", "r") as json_file:
    completed_season_goalamount = json.load(json_file)

    countries = ["ENG", "ESP", "FRA", "GER", "ITA"]
    seasons = ["14", "15", "16", "17", "18"]


with open("country_season_homefield_adv.csv", "r") as file:
    data = dict()
    for line in file:
        line = line.replace("\n", "")

        if line.startswith("country"):
            print(line + ";hf_adv_last_three_seasons")
            continue

        elements = line.split(";")

        hf_adv_last_seasons = 0.0

        if elements[1] == "14":
            hf_adv_last_seasons = 0.0
        if elements[1] == "15":
            hf_adv_last_seasons = float(completed_season_goalamount[elements[0]
                                                                    ]["14"]["mean"])
        if elements[1] == "16":
            hf_adv_last_seasons = float(
                completed_season_goalamount[elements[0]]["14"]["mean"] + completed_season_goalamount[elements[0]]["15"]["mean"]) / 2
        if elements[1] == "17":
            hf_adv_last_seasons = float(
                completed_season_goalamount[elements[0]]["14"]["mean"] + completed_season_goalamount[elements[0]]["15"]["mean"] + completed_season_goalamount[elements[0]]["16"]["mean"]) / 3
        if elements[1] == "18":
            hf_adv_last_seasons = float(
                completed_season_goalamount[elements[0]]["15"]["mean"] + completed_season_goalamount[elements[0]]["16"]["mean"] + completed_season_goalamount[elements[0]]["17"]["mean"]) / 3

        print(line + ";" + str(hf_adv_last_seasons))

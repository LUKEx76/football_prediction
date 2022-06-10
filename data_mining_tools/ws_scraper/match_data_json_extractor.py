import json
import os

path = "H:/Documents/Hochschule/Bachelorarbeit/ws_data/ita/2018-19/games"
directory = os.fsencode(path)

season = path.split("/")[-2].replace("20", "")
country = path.split("/")[-3].upper()

all_matches = []

for file in os.listdir(directory):
    data = None
    filename = os.fsdecode(file)
    with open(os.path.join(path, filename), "r", encoding="utf-8") as html:
        for line in html:
            if line.strip().startswith("var matchCentreData"):
                line = line.replace(
                    "var matchCentreData =", "").replace(";", "").strip()
                data = json.loads(line)

    if data == None:
        print("Error parsing json")
        exit()

    home_team_name = data["home"]["name"]
    away_team_name = data["away"]["name"]
    home_team_id = data["home"]["teamId"]
    away_team_id = data["away"]["teamId"]

    # raw_date = data["startDate"]
    # if " " in raw_date:
    #     start_date = raw_date.split(" ")[0]
    #     start_date = start_date.split(
    #         "/")[2] + "-" + raw_date.split("/")[0] + "-" + raw_date.split("/")[1]
    # else:
    #     start_date = raw_date[0:10]

    #score = data["score"]
    # if score == "vs":
    #     home_team_goals = "0 _bastia"
    #     away_team_goals = 0
    # else:
    # home_team_goals = score.split(":")[0].strip()
    # away_team_goals = score.split(":")[1].strip()

    # home_team_missed_shots = 0
    # away_team_missed_shots = 0
    # home_team_saved_shots = 0
    # away_team_saved_shots = 0

    # for event in data["events"]:
    #     if event["type"] != None:
    #         if event["teamId"] == home_team_id:
    #             if event["type"]["value"] == 13:  # MissedShot
    #                 home_team_missed_shots += 1
    #             if event["type"]["value"] == 15:  # SavedShot
    #                 home_team_saved_shots += 1
    #         elif event["teamId"] == away_team_id:
    #             if event["type"]["value"] == 13:  # MissedShot
    #                 away_team_missed_shots += 1
    #             if event["type"]["value"] == 15:  # SavedShot
    #                 away_team_saved_shots += 1

    home_team_shots_on_target = 0
    away_team_shots_on_target = 0
    home_team_shots_off_target = 0
    away_team_shots_off_target = 0
    home_team_shots_blocked = 0
    away_team_shots_blocked = 0

    if "shotsOnTarget" in data["home"]["stats"]:
        home_sont = data["home"]["stats"]["shotsOnTarget"]
        for key in home_sont:
            home_team_shots_on_target += int(home_sont[key])

    if "shotsOnTarget" in data["away"]["stats"]:
        away_sont = data["away"]["stats"]["shotsOnTarget"]
        for key in away_sont:
            away_team_shots_on_target += int(away_sont[key])

    if "shotsOffTarget" in data["home"]["stats"]:
        home_sofft = data["home"]["stats"]["shotsOffTarget"]
        for key in home_sofft:
            home_team_shots_off_target += int(home_sofft[key])

    if "shotsOffTarget" in data["away"]["stats"]:
        away_sofft = data["away"]["stats"]["shotsOffTarget"]
        for key in away_sofft:
            away_team_shots_off_target += int(away_sofft[key])

    if "shotsBlocked" in data["home"]["stats"]:
        home_sb = data["home"]["stats"]["shotsBlocked"]
        for key in home_sb:
            home_team_shots_blocked += int(home_sb[key])

    if "shotsBlocked" in data["away"]["stats"]:
        away_sb = data["away"]["stats"]["shotsBlocked"]
        for key in away_sb:
            away_team_shots_blocked += int(away_sb[key])

    print(f"'{country}';'{season}';'{home_team_name}';'{away_team_name}';{home_team_shots_on_target};{away_team_shots_on_target};{home_team_shots_off_target};{away_team_shots_off_target};{home_team_shots_blocked};{away_team_shots_blocked}")


# UTIL:
# events = data["events"]

# for event in events:
#     if event["type"] != None and event["type"]["displayName"] != None:
#         if event["type"]["displayName"] in ["Goal", "SavedShot", "MissedShot"]:
#             print(event)

# Code for Hierarchical Key Extraction
# for a in data.keys():
#     if len(a) > 2:
#         print(a)
#     if type(data[a]) is dict:
#         for b in data[a].keys():
#             if len(b) > 2:
#                 print("----", b)
#             if type(data[a][b]) is dict:
#                 for c in data[a][b].keys():
#                     if len(c) > 2:
#                         print("--------", c)
#                     if type(data[a][b][c]) is dict:
#                         for d in data[a][b][c].keys():
#                             if len(d) > 2:
#                                 print("------------", d)


from team_names import team_names_dict


with open('ita.csv', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.replace("'", "")
        elements = line.split(";")
        hometeamname = team_names_dict[elements[2]]
        awayteamname = team_names_dict[elements[3]]
        print(
            f"UPDATE matches SET hometeamshotsontarget = {elements[4]}, awayteamshotsontarget = {elements[5]}, hometeamshotsofftarget = {elements[6]}, awayteamshotsofftarget = {elements[7]}, hometeamshotsblocked = {elements[8]}, awayteamshotsblocked = {elements[9]} WHERE country = '{elements[0]}' AND season = '{elements[1]}' AND hometeamname = '{hometeamname}' AND awayteamname = '{awayteamname}';")

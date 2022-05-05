import os
import re
from bs4 import BeautifulSoup as soup


def cleanse_team_name(team_name):
    # team_name = team_name.replace("AFC", "").replace("FC", "").replace("Hotspur", "").replace(
    #     "Manchester", "Man").replace("United", "Utd").replace("Bromwich Albion", "Brom").replace("City", "").strip()
    # if team_name == "Man":
    #     team_name = "Man City"
    # team_name = team_name.replace("á", "a").replace(
    #     "é", "e").replace("í", "i").replace("ó", "o")
    # team_name = team_name.replace("UD", "").replace(
    #     "CD", "").replace("CA", "").replace("San Sebastian", "").strip()
    # team_name = team_name.replace("É", "E").replace("î", "i").replace("ß", "s")
    # team_name = team_name.replace("Stade", "").replace(
    #     "HSC", "").replace("Olympique", "").replace("AS", "").replace("Girondins", "").replace("OGC Nizza", "Nice").replace("RC", "").replace("SC", "").replace("Paris Saint-Germain", "PSG").replace("EA", "").replace("SM", "").replace("O ", "").replace(" O", "").replace("ESTAC", "").replace("LO", "").strip()
    # team_name = team_name.replace("München", "").replace(
    #     "önchen", ".").replace("VfB", "").replace("RasenBallsport", "RB").replace("ü", "ue").replace("1. Köln", "FC Cologne").replace("96", "").replace("98", "").replace("SV", "").replace("04", "").replace("TSG", "").replace("1899", "").replace("Bayer", "").replace("VfL", "").replace("1.FC", "").replace("05", "").replace("1.F", "").replace("SC", "").replace("FC", "").strip()
    team_name = team_name.replace("Rom", "Roma").replace("Bergamo", "").replace("Calcio", "").replace(
        "Florenz", "Fiorentina").replace("2013", "").replace("SPAL", "SPAL Ferrara").replace("Turin", "Torino").replace("FC", "").replace("ua C", "ua CFC").replace("SSC Neapel", "Napoli").replace("Genua", "Genoa").replace("Juventus Torino", "Juventus").replace("AC Mailand", "AC Milan").replace("AC", "").replace("Mailand", "").replace("1913", "").replace("US", "").strip()
    return team_name


path = "H:/Documents/Hochschule/Bachelorarbeit/tm_data/ita"
directory = os.fsencode(path)

country = path.split("/")[-1].upper()

all_data_rows = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    season = filename[-26:-21].replace("_", "-")
    if ".html" in filename:
        with open(os.path.join(path, filename), "r", encoding='utf-8') as html_file:
            print(f"-- {country} {season}")
            html_soup = soup(html_file.read(), "html.parser")
            club_value_table = html_soup.find_all(
                "table", {"class": "items"})[0]
            all_rows = club_value_table.find_next("tbody").find_all("tr")
            for row in all_rows:
                elements = row.find_all("td")
                team_name = cleanse_team_name(elements[1].text.strip())
                if "Mrd" in elements[6].text:
                    team_value = round(
                        float(elements[6].text.split("Mrd.")[0].replace(",", "."))*1000)
                else:
                    team_value = round(
                        float(elements[6].text.split("Mio.")[0].replace(",", ".")))
                avg_player_age = float(elements[3].text.replace(",", "."))
                print(
                    f"UPDATE teams SET valueinmio = {team_value}, avgplayerage = {avg_player_age} WHERE country = '{country}' AND season = '{season}' AND teamname = '{team_name}';")
        print()

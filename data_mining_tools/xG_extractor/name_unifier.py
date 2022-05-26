

def replace_team_name(line) -> str:
    line = line.replace('Roma', 'AS Roma')
    line = line.replace('Genoa', 'CFC Genoa')
    line = line.replace('Torino', 'FC Torino')
    line = line.replace('Verona', 'Hellas Verona')
    line = line.replace('SPAL 2013', 'SPAL Ferrara')
    return line


with open('us_ita.csv', 'r', encoding='utf-8') as file:
    for line in file:
        line = replace_team_name(line)
        elements = line.split(";")
        print(
            f"UPDATE matches SET hometeamxgs = {elements[4]}, awayteamxgs = {elements[5]} WHERE country = {elements[0]} AND season = {elements[1]} AND hometeamname = {elements[2]} AND awayteamname = {elements[3]};")

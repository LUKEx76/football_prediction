# mean_data = dict()
# with open("chance_mean.csv", "r") as file:
#     for line in file:
#         line = line.replace("\n", "")

#         if line.startswith("country"):
#             # print(line + ";market_value_ln_relative")
#             continue

#         elements = line.split(";")

#         if elements[0] not in mean_data.keys():
#             mean_data[elements[0]] = {}
#         if elements[1] not in mean_data[elements[0]].keys():
#             mean_data[elements[0]][elements[1]] = {}

#         mean_data[elements[0]][elements[1]] = elements[2]


data = dict()
with open("matches.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        elements = line.split(";")

        if line.startswith("country"):
            print(elements[0]+";"+elements[1]+";"+elements[2]+";" +
                  elements[3]+";"+elements[4]+";"+elements[5]+";"+elements[6]+";"+elements[7]+";is_promoter;"+elements[8]+";"+elements[9])
            continue

        is_promoter = False

        if elements[1] == "14" and elements[3] in ["Leicester", "Burnley", "Queens Park Rangers", "Eibar", "Depotivo La Coruna", "Cordoba", "Metz", "Lens", "Caen", "FC Cologne", "Paderborn", "Palermo", "Empoli", "Cesena"]:
            is_promoter = True
        if elements[1] == "15" and elements[3] in ["Norwich", "Watford", "Bournemouth", "Sporting Gijon", "Real Betis", "Las Palmas", "GFC Ajaccio", "Angers", "Troyes", "Darmstadt", "Ingolstadt", "Bologna", "Frosinone", "Carpi"]:
            is_promoter = True
        if elements[1] == "16" and elements[3] in ["Hull", "Burnley", "Middlesbrough", "Deportivo Alaves", "Osasuna", "Leganes", "Nancy", "Dijon", "Metz", "RB Leipzig", "Freiburg", "Pescara", "Cagliari", "Crotone"]:
            is_promoter = True
        if elements[1] == "17" and elements[3] in ["Newcastle", "Huddersfield", "Brighton", "Girona", "Levante", "Getafe", "Troyes", "Strasbourg", "Amiens", "Stuttgart", "Hannover", "Benevento", "Hellas Verona", "SPAL Ferrara"]:
            is_promoter = True
        if elements[1] == "18" and elements[3] in ["Fulham", "Wolves", "Cardiff", "SD Huesca", "Rayo Vallecano", "Real Valladolid", "Reims", "Nimes", "Nuernberg", "Fortuna Duesseldorf", "Parma", "Frosinone", "Empoli"]:
            is_promoter = True

        print(elements[0]+";"+elements[1]+";"+elements[2]+";" +
              elements[3]+";"+elements[4]+";"+elements[5]+";"+elements[6]+";"+elements[7]+";"+str(is_promoter).lower()+";"+elements[8]+";"+elements[9])

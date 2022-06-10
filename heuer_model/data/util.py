

with open('adv_per_match.csv', 'r', encoding='utf-8') as file:
    i = 0
    last_three_year = []
    for line in file:
        i += 1
        if line.startswith("season"):
            print(
                "season;matchnumber;recent_seasons_avg_hf_adv;seasons_avg_hf_adv;current_avg_hf_adv")
            continue
        elements = line.split(";")
        season_avg_home_field_adv = float(elements[1]) / float(elements[2])

        # last_three_years_home_field_adv = 0
        # if elements[0] == '14-15':
        #     last_three_years_home_field_adv = 0
        # elif elements[0] == '15-16':
        #     last_three_years_home_field_adv = float(674 / 1826)
        # elif elements[0] == '16-17':
        #     last_three_years_home_field_adv = float((
        #         674 / 1826 + 658 / 1826) / 2)
        # elif elements[0] == '17-18':
        #     last_three_years_home_field_adv = float((
        #         674 / 1826 + 658 / 1826 + 761 / 1826) / 3)
        # elif elements[0] == '18-19':
        #     last_three_years_home_field_adv = float((
        #         658 / 1826 + 761 / 1826 + 641 / 1826) / 3)

        print(
            f"{elements[0][0:2]};{season_avg_home_field_adv}")

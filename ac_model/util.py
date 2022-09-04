new_match = True
ht_data = []
with open("matches_ac.csv", "r") as file:
    for line in file:
        line = line.replace("\n", "")

        elements = line.split(";")

        if line.startswith("country"):
            print("country;season;matchnumber;ht_name;at_name;ht_curr_eff_chancediff;at_curr_eff_chancediff;ht_past_chancediff_combined;at_past_chancediff_combined;ht_curr_eff_chanceamount;at_curr_eff_chanceamount;ht_past_chanceamount;at_past_chanceamount;ht_market_value_ln_relative;at_market_value_ln_relative;ht_is_promoter;at_is_promoter;actual_goalamount;actual_goaldiff")
            continue

        if new_match:
            ht_data = elements

        if not new_match:
            print(elements[0] + ";" + elements[1] + ";" + elements[2] + ";" +
                  ht_data[3] + ";" + elements[3] + ";" +
                  ht_data[4] + ";" + elements[4] + ";" +
                  ht_data[5] + ";" + elements[5] + ";" +
                  ht_data[6] + ";" + elements[6] + ";" +
                  ht_data[7] + ";" + elements[7] + ";" +
                  ht_data[8] + ";" + elements[8] + ";" +
                  ht_data[9] + ";" + elements[9] + ";" +
                  ht_data[11] + ";" + ht_data[12] + ";")

        new_match = not new_match

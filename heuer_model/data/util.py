
stats = {}
with open('heuer_general.csv', 'r', encoding='utf-8') as file:
    i = 0
    for line in file:
        if line.startswith("country"):
            continue

        if i > 200:
            break

        elements = line.split(";")

        ht_goals, ht_sot = int(elements[6]), int(elements[8])
        at_goals, at_sot = int(elements[7]), int(elements[9])

        ht_chancedifference = ht_goals + ht_sot - at_goals - at_sot
        at_chancedifference = at_goals + at_sot - ht_goals - ht_sot

        if elements[0] == 'GER':
            ht_chancedifference = ht_chancedifference / 34
            at_chancedifference = at_chancedifference / 34
        else:
            ht_chancedifference = ht_chancedifference / 38
            at_chancedifference = at_chancedifference / 38

        season = elements[1][0:2]
        matchnumber = elements[2]
        ht = elements[4]
        at = elements[5]

        if season not in stats.keys():
            stats[season] = {}
        if matchnumber not in stats[season].keys():
            stats[season][matchnumber] = {}
        if ht not in stats[season][matchnumber]:
            stats[season][matchnumber][ht] = 0
        if at not in stats[season][matchnumber]:
            stats[season][matchnumber][at] = 0

        prev_matchnumber = str(int(matchnumber) - 1)

        if prev_matchnumber in stats[season].keys():
            if ht in stats[season][prev_matchnumber].keys():
                ht_chancedifference += stats[season][prev_matchnumber][ht]
            if at in stats[season][prev_matchnumber].keys():
                at_chancedifference += stats[season][prev_matchnumber][at]

        stats[season][matchnumber][ht] = ht_chancedifference
        stats[season][matchnumber][at] = at_chancedifference

        print(
            f"UPDATE standings SET avgchancedifference = {ht_chancedifference} WHERE season = '{elements[1]}' AND matchnumber = {matchnumber} AND teamname = '{ht}';")
        print(
            f"UPDATE standings SET avgchancedifference = {at_chancedifference} WHERE season = '{elements[1]}' AND matchnumber = {matchnumber} AND teamname = '{at}';")

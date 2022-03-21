from bs4 import BeautifulSoup as soup

with open("ENG_13_14.html") as html:
    page_soup = soup(html, "html.parser")
    scores = page_soup.findAll('td', {'class': 'table-score'})
    odds = page_soup.findAll('td', {'class': 'odds-nowrp'})

i = 0
for entry in scores:
    # print(
    #     f'(1) {odds[i].text.strip()}  (X) {odds[i+1].text.strip()}  (2) {odds[i+2].text.strip()} -> {entry.text.strip()}')
    score_as_vector = '[' + \
        entry.text.split(':')[0] + ',' + entry.text.split(':')[1] + ']'
    score_as_goal_difference = int(entry.text.split(
        ':')[0]) - int(entry.text.split(':')[1])
    print(
        f'{odds[i].text.strip()};{odds[i+1].text.strip()};{odds[i+2].text.strip()};{score_as_vector}')
    i = i + 3

print()
print(f'Num of DataPoints: {len(scores)}')
print(
    f'Validation: {len(scores)} = {int(len(odds) / 3)}')

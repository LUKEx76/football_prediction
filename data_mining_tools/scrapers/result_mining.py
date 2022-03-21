# Source OddsPortal.com
import requests

country = 'germany'
league = 'bundesliga'
season = '2013-2014'
max_pages = 7


page_count = 1
url = f'https://www.oddsportal.com/soccer/{country}/{league}-{season}/results/#/page/{page_count}/'


season_for_file = season.replace('-', '_')

with open(f'oddsportal/{league}/{season}/{league}_{season_for_file}.html', 'a') as file:
    for page_count in range(max_pages):
        html = requests.get(url)
        file.write('\n')
        file.write(html)
        page_count += 1

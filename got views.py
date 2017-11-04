from BeautifulSoup import BeautifulSoup
import urllib
import re
import random

views = 0

wiki = "https://en.wikipedia.org/wiki/Game_of_Thrones"
page = urllib.urlopen(wiki).read()
soup = BeautifulSoup(page)

read_wiki_table = soup.findAll('table', attrs={'class': 'wikitable'})
read_season_links = soup.findAll('a', attrs={'href': re.compile(('\/wiki\/Game_of_Thrones_\(season_?[0-9]+\)'))})

for season in read_season_links:
    season_url = "https://en.wikipedia.org" + season['href']
    season_html = urllib.urlopen(season_url).read()
    season_soup = BeautifulSoup(season_html)

    read_season_table = season_soup.find('table', attrs={'class': 'wikitable plainrowheaders wikiepisodetable'})

    if read_season_table:
        episode_tables = read_season_table.findAll('tr', attrs={'class': 'vevent'})

        for episode_table in episode_tables:
            episode_views = episode_table.findAll('td')[-1]
            views += float(re.sub(r'\[?[0-9]+\]', '', episode_views.text))

print str(views) + ' millions'
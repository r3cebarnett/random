import urllib.request
from bs4 import BeautifulSoup

urltmp = "http://www.espn.com/nba/salaries/_/year/{}/page/{}"
url = "http://www.espn.com/nba/salaries/_/year/2020/page/1"

with urllib.request.urlopen(url) as f:
    soup = BeautifulSoup(f, features='html.parser')

# Find page number
div = soup.findAll('div')
for i in div:
    if 'class' in i.attrs and i['class'][0] == 'page-numbers':
        saved = i

page, maxpage = list(map(int, saved.text.split()[0::2]))

tr = soup.findAll('tr')
for i in tr:
    if i['class'][0] == 'colhead':
        continue
    else:
        row = i.findAll('td')
        rank, player, team, salary = [j.get_text() for j in row]
        print(f"{rank}) {player} ({team}) - {salary}")

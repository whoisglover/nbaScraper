# #import libraries
# import urllib2
# from bs4 import BeautifulSoup

# original_url = 'http://www.vegasinsider.com/nba/teams/team-page.cfm/team/celtics'

# page = urllib2.urlopen(original_url)

# soup = BeautifulSoup(page, 'html.parser')


# table = soup.find('table', attrs={'width': '100%'})

# print(soup)

import urllib2
from bs4 import BeautifulSoup

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
response = opener.open('http://www.vegasinsider.com/nba/teams/team-page.cfm/team/celtics')
htmlSource = response.read()        
soup = BeautifulSoup(htmlSource, 'html.parser')                    
table_body = soup.find('tbody')
tables = soup.find_all('table', attrs={'width': '100%'})
max_rows = 0
max_table = None
for table in tables:
    trs = table.find_all('tr')
    if len(trs) >= max_rows:
        max_table = table
        max_rows = len(trs)

t_body = max_table.find_all('tbody')
t_rows = t_body[0].find_all('tr')
print "length:"
print len(t_rows)
for row in t_rows:
    t_datas = row.find_all('td')
    for td in t_datas:
        text = td.get_text().lstrip()
        print text
    print "----------"


# second = trs[1]
# second_tds = second.find_all('td')
# print len(second_tds)

# third = trs[2]
# third_tds = third.find_all('td')
# print len(third_tds)
    
# print len(table)
# # tr = td.find('tr')
# for elm in tr:
#     print elm 


# #import libraries
# import urllib2
# from bs4 import BeautifulSoup

# original_url = 'http://www.vegasinsider.com/nba/teams/team-page.cfm/team/celtics'

# page = urllib2.urlopen(original_url)

# soup = BeautifulSoup(page, 'html.parser')


# table = soup.find('table', attrs={'width': '100%'})

# print(soup)

#library to make network requests - aka download websites
import urllib2
#library to loop over html and grab stuff we want
from bs4 import BeautifulSoup


opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]



response = opener.open('http://www.vegasinsider.com/nba/teams/team-page.cfm/team/celtics')
htmlSource = response.read()        
soup = BeautifulSoup(htmlSource, 'html.parser')  
           
table_body = soup.find('tbody')

x = 5
y = 7

z = x + y
print z

print table_body

# x = [table1,table2,table3]
tables = soup.find_all('table', attrs={'width': '100%'})
# print tables

#find the biggest table
max_rows = 0
max_table = None
for table in tables:
    trs = table.find_all('tr') #tr = table row
    if len(trs) >= max_rows:
        max_table = table
        max_rows = len(trs)


#now we have max_table

t_body = max_table.find_all('tbody')
t_rows = t_body[0].find_all('tr')


print "length:"
print len(t_rows)
for row in t_rows:
    print "STARTING ROW"
    t_datas = row.find_all('td')
    csv_text_row = ""
    for td in t_datas:
        print "CSV TEXT ROW NOW:"
        print csv_text_row
        text = td.get_text().lstrip()
        csv_text_row = csv_text_row + text + ","
        
    print "-------------------"


#TO DO
# import csv library to create csv file 
# create a blank csv page
# for each data row create a csv string and add it to csv page

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


import requests
from bs4 import BeautifulSoup
import sqlite3
'''
 o
/|\
/ \
'''
#LINK TO SCRAPE FROM
for i in range(0, 250, 50):
    page = requests.get('https://myanimelist.net/topanime.php?limit='+format(i))
    #html content
    soup = BeautifulSoup(page.text, 'html.parser')
    elements = soup.find_all('tr', class_='ranking-list')
    for ele in elements:
        title = ele.find(class_='di-ib clearfix')
        rank = ele.find(class_='rank ac')
        rating = ele.find(class_='js-top-ranking-score-col di-ib al')
        
        new_title = title.text.strip()
        new_rank = rank.text.strip()
        new_rating = rating.text.strip()

        print(new_title + " Rank: " + new_rank + " Rating: " + new_rating)
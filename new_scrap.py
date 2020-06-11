from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

site = 'https://news.google.com/news/rss'
op = urlopen(site) #Open that site
rd = op.read() #read data from site
op.close()   # close the object
sp_page = soup(rd,'xml') #scrapping data from site
news_list = sp_page.find_all('item') #finding news
for news in news_list:  #printing news
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print('-'*60)
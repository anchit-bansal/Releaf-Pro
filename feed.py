"""
Necessary imports for feed parsing, reading html pages, read/write to .csv files
"""
from lxml import html
import random
import time
import requests
import feedparser
import pandas as pd
##############################################################################################################################
"""
RSS feed urls of all categories on allafrica.com
"""
feedparser.USER_AGENT="Mozilla/5.0 +http://google.com/"
urls = ["http://allafrica.com/tools/headlines/rdf/business/headlines.rdf","http://allafrica.com/tools/headlines/rdf/arts/headlines.rdf","http://allafrica.com/tools/headlines/rdf/africa/headlines.rdf",
"http://allafrica.com/tools/headlines/rdf/centralafrica/headlines.rdf","http://allafrica.com/tools/headlines/rdf/eastafrica/headlines.rdf","http://allafrica.com/tools/headlines/rdf/northafrica/headlines.rdf","http://allafrica.com/tools/headlines/rdf/southernafrica/headlines.rdf"
,"http://allafrica.com/tools/headlines/rdf/conflict/headlines.rdf","http://allafrica.com/tools/headlines/rdf/environment/headlines.rdf","http://allafrica.com/tools/headlines/rdf/health/headlines.rdf","http://allafrica.com/tools/headlines/rdf/sport/headlines.rdf","http://allafrica.com/tools/headlines/rdf/travel/headlines.rdf",
"http://allafrica.com/tools/headlines/rdf/aid/headlines.rdf","http://allafrica.com/tools/headlines/rdf/education/headlines.rdf","http://allafrica.com/tools/headlines/rdf/agriculture/headlines.rdf","http://allafrica.com/tools/headlines/rdf/women/headlines.rdf","http://allafrica.com/tools/headlines/rdf/agribusiness/headlines.rdf",
"http://allafrica.com/tools/headlines/rdf/banking/headlines.rdf","http://allafrica.com/tools/headlines/rdf/capitalflows/headlines.rdf","http://allafrica.com/tools/headlines/rdf/commodities/headlines.rdf","http://allafrica.com/tools/headlines/rdf/company/headlines.rdf","http://allafrica.com/tools/headlines/rdf/construction/headlines.rdf",
"http://allafrica.com/tools/headlines/rdf/currencies/headlines.rdf","http://allafrica.com/tools/headlines/rdf/debt/headlines.rdf","http://allafrica.com/tools/headlines/rdf/energy/headlines.rdf","http://allafrica.com/tools/headlines/rdf/infrastructure/headlines.rdf","http://allafrica.com/tools/headlines/rdf/investment/headlines.rdf",
"http://allafrica.com/tools/headlines/rdf/labour/headlines.rdf","http://allafrica.com/tools/headlines/rdf/manufacturing/headlines.rdf","http://allafrica.com/tools/headlines/rdf/mining/headlines.rdf","http://allafrica.com/tools/headlines/rdf/ict/headlines.rdf","http://allafrica.com/tools/headlines/rdf/petroleum/headlines.rdf",
"http://allafrica.com/tools/headlines/rdf/privatization/headlines.rdf","http://allafrica.com/tools/headlines/rdf/stockmarkets/headlines.rdf","http://allafrica.com/tools/headlines/rdf/trade/headlines.rdf","http://allafrica.com/tools/headlines/rdf/transport/headlines.rdf","http://allafrica.com/tools/headlines/rdf/innovation/headlines.rdf",
"http://allafrica.com/tools/headlines/rdf/sustainable/headlines.rdf","http://allafrica.com/tools/headlines/rdf/bookreviews/headlines.rdf","http://allafrica.com/tools/headlines/rdf/books/headlines.rdf","http://allafrica.com/tools/headlines/rdf/music/headlines.rdf","http://allafrica.com/tools/headlines/rdf/musicreviews/headlines.rdf","http://allafrica.com/tools/headlines/rdf/athletics/headlines.rdf",
"http://allafrica.com/tools/headlines/rdf/olympics/headlines.rdf","http://allafrica.com/tools/headlines/rdf/soccer/headlines.rdf","http://allafrica.com/tools/headlines/rdf/worldcup/headlines.rdf","http://allafrica.com/tools/headlines/rdf/asiaaustraliaandafrica/headlines.rdf","http://allafrica.com/tools/headlines/rdf/europeandafrica/headlines.rdf","http://allafrica.com/tools/headlines/rdf/io/headlines.rdf",
"http://allafrica.com/tools/headlines/rdf/latinamericaandafrica/headlines.rdf","http://allafrica.com/tools/headlines/rdf/middleeastandafrica/headlines.rdf","http://allafrica.com/tools/headlines/rdf/usafrica/headlines.rdf","http://allafrica.com/tools/headlines/rdf/corruption/headlines.rdf","http://allafrica.com/tools/headlines/rdf/governance/headlines.rdf",
"http://allafrica.com/tools/headlines/rdf/humanrights/headlines.rdf","http://allafrica.com/tools/headlines/rdf/land/headlines.rdf","http://allafrica.com/tools/headlines/rdf/legalaffairs/headlines.rdf","http://allafrica.com/tools/headlines/rdf/media/headlines.rdf","http://allafrica.com/tools/headlines/rdf/ngo/headlines.rdf"]
##############################################################################################################################
"""
Scraping data from allafrica.com resulted in me getting blocked many times so had to keep rotating my IP and set my host agent
"""
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
proxies_list = ["128.199.109.241:8080","113.53.230.195:3128","125.141.200.53:80","125.141.200.14:80","128.199.200.112:138","149.56.123.99:3128","128.199.200.112:80","125.141.200.39:80","134.213.29.202:4444"]
##############################################################################################################################
"""
Empty list for links to all articles present on allafrica.com
"""
links=[]
##############################################################################################################################
"""
Using PANDAS to read and write to csv files
"""
df = pd.read_csv('SAMPLE_DATA.csv')		#Reading SAMPLE_DATA file
names = df.Name.tolist()					#Extracting the name of companies from Name column
col=['Name','URL']
wf = pd.DataFrame(index=None,columns=col)	#Dataframe for new .csv file
##############################################################################################################################
from bs4 import BeautifulSoup
i=0
for url in urls:													#Parsing each URL
	d=feedparser.parse(url)
	print url
	for a in d.entries:			
		#time.sleep(0.5 * random.random())							#Random sleep time to prevent being seen as a bot
		links.append(a['link'])										#Getting links to articles on each rss feed URL
links=list(set(links))											#Removing duplicates for efficiency
print len(links)
for pg in links:
	proxies = {'https': random.choice(proxies_list)}			#Random proxy
	page=requests.get(pg,headers=headers,proxies=proxies)		
	#time.sleep(0.5 * random.random())
	soup = BeautifulSoup(page.content,'lxml')
	page=''
	for p in soup.find_all('p'):
		page=page+p.get_text()									#Getting all visible text in the article
	page=page.encode('utf-8')
	for name in names:
		if not isinstance(name, float):
			print "Checking " + name + " in " + pg + "\n"
			if name in page:									#Searching company's name in the article
				wf.loc[i]=[name,pg]								#If found add aricle's URL and Company's name in the dataframe
				i=i+1
				print "Found " + name + " in " + pg + "\n"
final=pd.merge(df,wf)												#Merge both dtaframes
final.to_csv('Final.csv',index=False)								#Writing merged dataframe to .csv file
# Releaf-Pro
Assessment Project for summer internship at Releaf

The feed.py scraps all rss feeds on allafrica.com for company names in SAMPLE_DATA.csv and creates a new .csv file (Final.csv) containing the urls of the articles where company's name was found.

The feed.py uses:
FeedParser
BeautifulSoup
Pandas

The current Final.csv file is output of feed.py where on finding the Company's name the URL of that article and the company name from SAMPLE_DATA.csv will be added but since nothing was found the Final.csv is empty. The running of the script for this scenario is demonstrated in Demo_Project.

For proper implementation demonstration output_africa.csv file contains the output of feed.py where on finding the keyword 'Bank' the URL of that articles (found from the 1st feed) and the kryword 'Bank' is added.The running of the script for this scenario is demonstrated in Demo_Project_Africa.

Proper comments in feed.py have been provided wherever felt necesssary.

Screenshots folder contains some pictures of script running.

The script not only searches for company’s name in the articles related to the sector in which company dominates but instead searches all the articles for better coverage, this definitely is a time consuming process but covers all exceptional cases and there is lot of improvement possible in the algorithm.

# News Parser
This tool allows you to log the main titles of news sites in Israel.

The implementation is based on [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

## Installation
This tool is based on Python version 3.5 and above.

to use the tool install the requirements file with pip in the following way:
```
pip install -r requirements.txt 
```

## Usage
for basic usage you can use news_parser.py as an command line tool. 
for example, if you'll want to scarp the titles of ynet every 60 seconds you could use:
```
python news_parser.py ynet 60
```
Note: Please don't use any time that is less than 60 seconds or it might being consider as an attack by the news site.

### Available modes
1. ynet - logs [ynet](https://www.ynet.co.il/home/0,7340,L-8,00.html)
2. haaretz - logs [הארץ](https://www.haaretz.co.il/)
2. kikar - logs [כיכר השבת](https://www.kikar.co.il/)

Legal notes
---------------------------------------
This tool is considered a [web scarper](https://en.wikipedia.org/wiki/Web_scraping), 
please use it in an [ethical](https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01) way 
AND according to the [Israeli law](http://legalstart.idc.ac.il/he/web-scraping-%D7%91%D7%93%D7%99%D7%9F-%D7%94%D7%99%D7%A9%D7%A8%D7%90%D7%9C%D7%99/)

I'm not responsible for any misusing of that tool.
from urllib import request
from bs4 import BeautifulSoup
import logging
import time
import sys


class NewsLogger:
    def __init__(self, mode):
        self.mode = mode
        self._initialize_logger()

    def _initialize_logger(self):
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        fh = logging.FileHandler(self.mode + '.log', 'a')
        fh.setFormatter(formatter)

        self.logger = logging.getLogger(self.mode + '_app')
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(fh)

    def _soup_from_url(self, url):
        html = request.urlopen(url)
        return BeautifulSoup(html, 'html.parser')

    def _log_title(self, soup, tag, attrs, name):
        for a in soup.find_all(tag, attrs=attrs):
            text = a.text.strip()
            self.logger.info(name + ' - ' + text)

    def log_site(self):
        if self.mode == 'ynet':
            soup = self._soup_from_url('https://www.ynet.co.il/home/0,7340,L-8,00.html')
            self._log_title(soup, 'span', {'class': 'subtitle'}, 'main')
            self._log_title(soup, 'div', {'class': 'title', 'style': 'color:#FFFFFF;'}, 'Secondary')
        elif self.mode == 'haaretz':
            soup = self._soup_from_url('https://www.haaretz.co.il/')
            self._log_title(soup, 'h1', {'class': 't-gamma t-beta--xl h-mb--xxtight--xl'}, 'main')
            self._log_title(soup, 'h3', {'class': 't-delta h-mb--xxtight'}, 'secondary')
            self._log_title(soup, 'h3', {'class': 't-epsilon h-mb--xxtight--l'}, 'tertiary')

    def log_in_interval(self, sleep_time):
        # Using sleep_time < 60 might be considered as an attack
        while True:
            self.log_site()
            print('logging ' + self.mode)
            time.sleep(sleep_time)


if __name__ == '__main__':
    args_num = len(sys.argv)
    if args_num == 3:
        ynet_logger = NewsLogger(sys.argv[1])
        ynet_logger.log_in_interval(int(sys.argv[2]))
    else:
        print('usage:')
        print('news_parser.py <parser_mode> <logging_interval>')
        print('<parser_mode>        the name of the site you want to log')
        print('<logging_interval>   the interval of logging the site (in seconds)\n')
        print('for example:')
        print('* python news_parser.py ynet 100\n')
        print('available parsers:')
        print('* ynet - www.ynet.co.il')
        print('* haaretz - www.haaretz.co.il\n')
        print('Important notes:')
        print('* Please don\'t use logging_interval < 60')

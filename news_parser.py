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

    def log_site(self):
        if self.mode == 'ynet':
            html = request.urlopen('https://www.ynet.co.il/home/0,7340,L-8,00.html')
            soup = BeautifulSoup(html, 'html.parser')

            for a in soup.find_all('span', attrs={'class': 'subtitle'}):
                text = a.text.strip()
                self.logger.info('main - ' + text)
            for a in soup.find_all('div', attrs={'class': 'str3s_txt'}):
                text = [b for b in a.children][0].text.strip()
                self.logger.info('Secondary - '.format() + text)

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
        print('* ynet - www.ynet.co.il\n')
        print('Important notes:')
        print('* Please don\'t use logging_interval < 60')

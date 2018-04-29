from bs4 import BeautifulSoup
import re

class MParser(object):
    def __init__(self, url = None):
        self.base_url = url or "https://github.com"

    def parse(self, content):
        target_urls = list()
        urls = list()
        soup = BeautifulSoup(content, 'html.parser')
        for item in soup.find_all(itemprop = "name codeRepository"):
            target_urls.append(self.base_url+str(item.get('href')))
        
        for item in soup.find_all("a",class_ = "next_page"):
            urls.append(self.base_url+str(item.get("href")))

        return urls, target_urls




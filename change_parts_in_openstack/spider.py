import threading
import time 
import urllib2
from bs4 import BeautifulSoup
import constants
import logging
 
class Spider(threading.Thread):
    def __init__(self,thread_pool):
        threading.Thread.__init__(self) 
        self.thread_pool = thread_pool
        self.base_url = "https://github.com"
        self.logger = logging.getLogger('spider.Spider')
        self.logger.info('creating an instance of spider')
        self.logger.setLevel(logging.INFO)
        # create file handler which logs even debug messages
        fh = logging.FileHandler('spider.log')
        fh.setLevel(logging.INFO)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def run(self):
        thread_pool = self.thread_pool
        while(True):
            try: 
                page_url = "".join(thread_pool.get_page_url())
                #page_url = https://github.com/openstack?page=2
            except Exception:
                thread_pool.put_page_url(page_url)
                continue
            try:    
                content = urllib2.urlopen(url=page_url).read()
                soup = BeautifulSoup(content,'html.parser')
                for item in soup.find_all(itemprop = "name codeRepository"):
                    thread_pool.put_git_url([self.base_url,str(item.get("href")),".git"])
                    #page_url = [https://github.com/openstack,/sahara-dashboard,.git]
                    thread_pool.add_git_url_count()
                for item in soup.find_all("a",class_ = "next_page"):
                    thread_pool.put_page_url([self.base_url,str(item.get("href"))])
                    #git_url = [https://github.com,/openstack?page=2]
                    thread_pool.add_page_count()
            except Exception as e:    
                print e
            if thread_pool.page_urls.qsize() <= 0:
                time.sleep(constants.SPIDER_COUNT)    
                if thread_pool.page_urls.qsize() <= 0:
                    break
                    
            
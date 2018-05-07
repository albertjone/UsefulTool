import threading
import time 
import urllib2
from bs4 import BeautifulSoup
import constants

 
class Spider(threading.Thread):
    def __init__(self,thread_pool):
        threading.Thread.__init__(self) 
        self.thread_pool = thread_pool
        self.base_url = "https://github.com"
    def run(self):
        thread_pool = self.thread_pool
        while(True):
            try: 
                page_url = thread_pool.get_page()
                content = urllib2.urlopen(url=page_url).read()
                soup = BeautifulSoup(content,'html.parser')
                for item in soup.find_all(itemprop = "name codeRepository"):
                    thread_pool.put_git_url(self.base_url+str(item.get("href")))
                    thread_pool.add_git_url_count()
                for item in soup.find_all("a",class_ = "next_page"):
                    thread_pool.put_page_url(self.base_url+str(item.get("href")))
                    thread_pool.add_page_count()
            except Exception as e:
                print e
            if thread_pool.page_urls.qsize() <= 0:
                time.sleep(constants.SPIDER_COUNT)    
                if thread_pool.page_urls.qsize() <= 0:
                    break
                    
            
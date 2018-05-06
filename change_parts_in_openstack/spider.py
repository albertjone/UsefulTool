import threading
import time 
import urllib2
from bs4 import BeautifulSoup

 
class Spider(threading.Thread):
    def __init__(self,thread_pool):
        threading.Thread.__init__(self) 
        self.thread_pool = thread_pool
        self.base_url = "https://github.com"
    def run(self):
        thread_pool = self.thread_pool
        while(True):
            time.sleep(10)
            try: 
                page_url = thread_pool.get_page()
                content = urllib2.urlopen(url=page_url).read()
                soup = BeautifulSoup(content,'html.parser')
                for item in soup.find_all(itemprop = "name codeRepository"):
                    thread_pool.put_git_url(self.base_url+str(item.get("href")))
                for item in soup.find_all("a",class_ = "next_page"):
                    thread_pool.put_page_url(self.base_url+str(item.get("href")))
            except Exception as e:
                print e
            if thread_pool.page_urls.qsize() <= 0:
                break    

            
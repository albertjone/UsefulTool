from scheduler import Scheduler
from downloader import Downloader
from mparser import MParser
import os
import git
from multiprocessing import Pool
class Manager(object):
    def __init__(self,start_url = None):
        self.parser = MParser()
        self.downloader = Downloader()
        self.scheduler = Scheduler()
        self.target_urls = list()
        self.start_url = start_url
    @staticmethod    
    def gitclone(url,path):
        git.Git(path).clone(url+".git")

    @classmethod
    def download(cls, urls,path):
        p = Pool(10)
        p.map(cls.gitclone, urls)
        

    def run(self):
        self.scheduler.add_new_urls(self.start_url)
        while self.scheduler.has_url():
            url = self.scheduler.get_url()
            content = self.downloader.download(url)
            urls, target_urls = self.parser.parse(content)
            self.scheduler.add_new_urls(urls)
            for url in target_urls:
                self.target_urls.append(url)
        
        if not os.path.isdir("C:\\Users\\Mr.Guan\\Desktop\\OpenstackREP\\"):
            path = os.mkdir(path="C:\\Users\\Mr.Guan\\Desktop\\OpenstackREP\\")
            os.chdir(path)
        else:
            os.chdir("C:\\Users\\Mr.Guan\\Desktop\\OpenstackREP\\")   
        try:
            Manager.download(urls = self.target_urls,path = path)
        except Exception as e:
            print(e)


def main():
    manager = Manager("https://github.com/openstack")
    manager.run()




if __name__ == "__main__":
    main()






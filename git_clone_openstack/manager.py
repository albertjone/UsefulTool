from scheduler import Scheduler
from downloader import Downloader
from mparser import MParser
import os
import git
# from multiprocessing import Process,Lock
from multiprocessing import Pool
class Manager(object):
    def __init__(self,start_url = None):
        self.parser = MParser()
        self.downloader = Downloader()
        self.scheduler = Scheduler()
        
        self.target_urls = list()
        self.start_url = start_url
        self.page = 1 

        

    def run(self):
        self.scheduler.add_new_url(self.start_url)
        # while self.scheduler.has_url():
        count = 1
        while count <=30:
            
            url = self.scheduler.get_url()
            print("get page"+str(self.page)+":"+url)
            if not url:
                self.page += 1
            try:
                content = self.downloader.download(url)
                urls, target_urls = self.parser.parse(content)
                for url in urls:
                    self.scheduler.add_new_url(url)
                for url in target_urls:
                    self.target_urls.append(url)
                count += 1
            except Exception as e:
                print("get total"+str(count)+"pages")
        print("get total:"+str(len(self.target_urls)))
        print(self.target_urls[6])
        
        if os.name == "posix":
            print("your current system is posix")
            path = "/root/GXJ/UsefulTool"
            if not os.path.isdir(path):
                print("begin to create repository ")
                path = os.mkdir(path)
                print("repository is created")
                os.chdir(path)
                print("current folder is :"+os.path.curdir())
            else:
                print("the destination exits")
                os.chdir(path)
        else:
            print("your current system is windowshood")
            path = "C:\\Users\\Mr.Guan\\Desktop\\OpenstackREP\\"
            if not os.path.isdir():
                print("begin to create repository ")
                path = os.mkdir(path)
                print("repository is created")
                os.chdir(path)
                print("current folder is :"+os.path.curdir())
            else:
                os.chdir(path)   
        print("repository created")
        return self.target_urls


def gitclone(url):
    if not os.path.isdir(url):
        print("current download git is:"+url)
        git.Git("/root/GXJ/UsefulTool").clone(url+".git")


def main():
    count = 0
    manager = Manager("https://github.com/openstack")
    target_urls = manager.run()
    p = Pool(5)  
    pool = Pool(10)
    pool.map(gitclone, target_urls)
    

    # for target in target_urls:
    #     Process(target=gitclone,args=(target,lock,count)).start()
     



if __name__ == "__main__":
    main()






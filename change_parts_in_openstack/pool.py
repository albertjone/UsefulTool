import Queue
import constants
from spider import Spider
from gitcloner import GitCloner
from updater import Updater
from searcher import Searcher
from commiter import Commiter
import time 


class Pool(object):
    def __init__(self):
        self.page_urls = Queue.Queue()
        self.git_urls = Queue.Queue()
        self.git_folders = Queue.Queue()
        self.git_finds = Queue.Queue()
        self.git_commits = Queue.Queue()
        self.git_search_folder = Queue.Queue()
        self.old_pages = [] 
        self.fail_path = []

        self.page_count = 0
        self.git_url_count = 0
        self.git_folder = 0
        self.git_find = 0
        self.git_commit = 0
        self.git_search_folder_count = 0
        

        self.spider_count = 0
        self.gitcloner_count = 0
        self.updater_count = 0
        self.searcher_count = 0
        self.commiter_count = 0


        self.spider_processes = []
        self.gitcloner_processes = []
        self.updater_processes = []
        self.searcher_processes = []
        self.commiter_processes = []
        self.processes = []
        self.__init_thread_pool()


        self.page_count = 0
        self.git_url_count = 0
        self.git_folder_count = 0
        self.git_find_count = 0
        self.git_commit_count = 0
        self.git_search_folder_count = 0        
        
    def add_fail_path(self,file_path):
        self.fail_path.append(file_path)

    def get_fail_path(self):
        return self.fail_path.pop()


    def add_page_count(self):
        self.page_count += 1
    
    def add_git_url_count(self):
        self.git_url_count += 1
    

    def add_git_folder_count(self):
        self.git_folder_count += 1
    
    def add_git_find_count(self):
        self.git_find_count += 1

    
    def add_commit_count(self):
        self.git_commit_count +=1
    
    def add_search_folder_count(self):
        self.git_search_folder_count += 1

    def get_page_count(self):
        self.page_count += 1
    
    
    def get_git_url_count(self):
        self.git_url_count += 1
    

    def get_git_folder_count(self):
        self.git_folder_count += 1
    
    def get_git_find_count(self):
        self.git_find_count += 1

    
    def get_commit_count(self):
        self.git_commit_count +=1
    
    def get_search_folder_count(self):
        self.git_search_folder_count += 1


        
    #initial processes pool
    def __init_thread_pool(self):
        self.page_urls.put(constants.START_URL)
        
        for i in range(constants.SPIDER_COUNT):
            self.spider_processes.append(Spider(self))
        for i in range(constants.GITCLONER_COUNT):
            self.gitcloner_processes.append(GitCloner(self))
        for i in range(constants.UPDATER_COUNT):
            self.updater_processes.append(Updater(self))
        for i in range(constants.SEARCHER_COUNT):
            self.searcher_processes.append(Searcher(self))
        for i in range(constants.COMMITER_COUNT):
            self.commiter_processes.append(Commiter(self))



    def wait_all_complete(self):
        for item in self.processes:
            if item.isAlive():
                item.join()

    #start process 
    def start_task(self):

        for item in self.spider_processes:
            item.start()
        time.sleep(constants.CLONER_DELAY)
        for item in self.gitcloner_processes:
            item.start()
        time.sleep(constants.SEARCHER_COUNT)
        for item in self.searcher_processes:
            item.start()
        time.sleep(constants.COMMITER_DELAY)
        for item in self.commiter_processes:
            item.start()
        time.sleep(constants.UPDATER_DELAY)
        for item in self.updater_processes:
            item.start()

    def get_page_url(self):
        page_url = self.page_urls.get()
        self.old_pages.append(page_url)
        return page_url

    # can not make sure the page putted into the queue is unique
    def put_page_url(self,page):
        if not page in self.old_pages:
            self.page_urls.put(page)
        else:
            return

    def get_git_url(self):
        git_url = self.git_urls.get()
        return git_url
    
    def put_git_url(self,git_url):
        self.git_urls.put(git_url)
    
    def get_git_folder(self):
        git_folder = self.git_folders.get()
        return git_folder

    def put_git_folder(self,git_folder):
        self.git_folders.put(git_folder)

    def get_git_find(self):
        git_find = self.git_finds.get()
        return git_find
    
    def put_git_find(self,git_find):
        self.git_finds.put(git_find)


    def get_git_search_folder(self):
        git_search_folder = self.git_search_folder.get()
        return git_search_folder
    
    def put_git_search_folder(self,git_search_folder):
        self.git_search_folder.put(git_search_folder)
        

    def get_git_commit(self):
        git_commit = self.git_commits.get()
        return git_commit
    def put_git_commit(self,git_commit):
        self.git_commits.put(git_commit)





import threading
import constants
import os
import git
import time
import logging
import logging.handlers


class GitCloner(threading.Thread):
    def __init__(self,thread_pool):
        threading.Thread.__init__(self)
        self.thread_pool = thread_pool
        self.repository_folder = constants.REPOSITORY_FOLDER
    def run(self):
        repository_folder = self.repository_folder
        if not os.path.isdir(self.repository_folder):
            os.mkdir(repository_folder)
        os.chdir(repository_folder)
        while(True):
            git_url = self.thread_pool.get_git_url()
            git_url_str = "".join(git_url)
            try:
                if not os.path.isdir(git_url[1]):
                    git.Git(repository_folder).clone(git_url_str)
                    self.thread_pool.put_git_folder(git_url[1])
                    self.thread_pool.put_git_search_folder(git_url[1])
            except Exception as e:
                print("error in process gitclone")
                print e
                self.thread_pool.put_git_url(git_url[1])
            if self.thread_pool.git_urls.qsize <= 0:
                time.sleep(constants.GITCLONER_COUNT)
                if self.thread_pool.git_urls.qsize <= 0:
                    break
        
            
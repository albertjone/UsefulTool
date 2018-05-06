import threading
import constants
import os
import git
import time
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
            time.sleep(10)
            git_url = self.thread_pool.get_git_url()
            try:
                if not os.path.isdir(git_url):
                    git.Git(repository_folder).clone(git_url+".git")
            except Exception:
                print("error in process gitclone")
            if self.thread_pool.git_urls.qsize <= 0:
                break
        
            
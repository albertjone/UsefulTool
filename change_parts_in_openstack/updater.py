import threading 
import os
import time
import constants
import git

class Updater(threading.Thread):
    def __init__(self,thread_pool):
        threading.Thread.__init__(self)
        self.thread_pool = thread_pool


    def run(self):
        if not os.path.isdir(constants.REPOSITORY_FOLDER):
            os.mkdir(constants.REPOSITORY_FOLDER)
        folders = os.listdir(constants.REPOSITORY_FOLDER)
        for folder in folders:
            self.thread_pool.put_git_folder(folder)
            self.thread_pool.add_git_folder_count()
        while(True):
            time.sleep(7200)
            repo = git.Repo(self.repository+'/'+self.thread_pool.get_git_folder)
            origin = repo.remotes.origin
            origin.pull()
            if self.thread_pool.git_folders.qsize() <= 0:
                break
            

        
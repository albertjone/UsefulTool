import threading
import time 
import git
import constants
import os 

class Commiter(threading.Thread):
    def __init__(self,thread_pool):
        threading.Thread.__init__(self)
        self.thread_pool = thread_pool
    def run(self):
        while(True):
            time.sleep(constants.COMMIT_WAIT)
            try:
                commit_folder = os.path.join(constants.REPOSITORY_FOLDER,
                                            self.thread_pool.get_git_commit()) 
                
                os.chdir("/home/openstack/Desktop/Openstack/performance-docs")
                print("in commit progress")
                print(os.getcwd())
                os.system("git add .")
                os.system('git commit --message="Trivial: Update pypi url to new url"')
                os.system('git review')
            except Exception:
                print("problem in commit progress")
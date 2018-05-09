import threading
import time 
import git
import constants
import os 
import commands
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
                
                os.chdir(commit_folder)
                if(commands.getstatusoutput(" git add .")[0] != 0):
                    print("add fails")
                    continue
                if(commands.getstatusoutput('git commit --message="Trivial: Update pypi url to new url"')[0] !=0):
                    print("commit fails")
                    continue
                print(commands.getstatusoutput('git review'))
                if (commands.getstatusoutput('git review')[0] != 0):
                    print("git review fail")
                    self.thread_pool.put_git_commit(commit_folder)
                    commands.getstatusoutput("git reset --hard HEAD^")
                
            except Exception:
                print("problem in commit progress")
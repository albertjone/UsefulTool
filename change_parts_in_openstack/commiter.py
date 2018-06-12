import threading
import time 
import git
import constants
import os 
import commands
import logging
class Commiter(threading.Thread):
    def __init__(self,thread_pool):
        threading.Thread.__init__(self)
        self.thread_pool = thread_pool
        self.logger = logging.getLogger('commiter.Commiter')
        self.logger.info('creating an instance of Commiter')
        self.logger.setLevel(logging.INFO)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(constants.LOGPATH+'commiter.log')
        fh.setLevel(logging.INFO)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def run(self):
        while(True):
            try:
                commit_folder = os.path.join(constants.REPOSITORY_FOLDER,
                                            self.thread_pool.get_git_commit()[1])                
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
                    self.logger.info("failed to commit"+commit_folder+
                                        "current commit_folder's size is:"+
                                        str(self.thread_pool.get_git_folder_count))
                    commands.getstatusoutput("git reset --hard HEAD^")
                
            except Exception as e:
                self.logger.ifno('error in commiter'+e)
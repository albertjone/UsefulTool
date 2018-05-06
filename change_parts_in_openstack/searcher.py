import threading
import constants
import os
import time 
import commands
import re

class Searcher(threading.Thread):
    def __init__(self,thread_pool):
        threading.Thread.__init__(self)
        self.thread_pool = thread_pool
        self.patten = constants.PATTEN
        self.search_wait = constants.SEARCH_WAIT
    
    def __init_search_folder(self):
        search_folders = os.listdir(constants.REPOSITORY_FOLDER)
        for folder in search_folders:
            self.thread_pool.put_git_search_folder(folder)


    def run(self):

        self.__init_search_folder()
        while(True):
            time.sleep(self.search_wait)
            try:
                git_folder = self.thread_pool.get_git_search_folder()
                os.chdir(git_folder)
                self.__replace_dest_with_certain(constants.REPOSITORY_FOLDER+git_folder,constants.PATTEN,constants.REPLACEMENT)
            except Exception:
                print "things are wrong in searcher process"
            self.thread_pool.put_git_commit(git_folder)
            if self.thread_pool.git_search_folder.qsize() <= 0:
                break

    def __replace_dest_with_certain(self,path = None, patten = None,repl = None):
        if path is None:
            print "path is None"
            return
        if not os.path.isdir():
            print "path is not a folder"
            return
        arr = path.split('/')
        if not arr[-1].startswith('.'): 
            terms = os.listdir(path)
            for term in terms:
                path = os.path.join(path,term)
                if os.path.isdir(path):
                    self.__replace_dest_with_certain(path,patten,repl)
                else:
                    if path.split('.')[-1].lower() in constants.FILE_TYPE:
                        return
                    data = open(path).read()
                    data = re.sub(patten,repl,data)
                    print("data in searcher progress"+ data)
                    open(path,'wb').write(data)

                    
                
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

    def _replace_dest_with_certain(self,path = None, patten = None,repl = None):
        if path is None:
            print "path is None"
            return
        all_file_list = os.listdir(path)
        for file in all_file_list:
            file_path = os.path.join(path,file)
            if os.path.isdir(file_path):
                self._replace_dest_with_certain(file_path,patten=patten,repl=repl)     
            else:
                if not file_path.split('.')[-1].lower() in constants.FILE_TYPE:
                    try:     
                        data = open(file_path).read()
                        new_data = re.sub(patten,repl,data)
                        open(file_path,'wb').write(new_data)
                        if data != new_data:
                            print(file_path) 
                    except Exception :
                        print("failure path:"+file_path)

                    
                
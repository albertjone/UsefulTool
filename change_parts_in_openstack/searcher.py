import threading
import constants
import os
import time 
import commands
import re
import logging

class Searcher(threading.Thread):
    def __init__(self,thread_pool):
        threading.Thread.__init__(self)
        self.thread_pool = thread_pool
        self.patten = constants.PATTEN
        self.search_wait = constants.SEARCH_WAIT
        self.logger = logging.getLogger('searcher.Searcher')
        self.logger.info('creating an instance of Searcher')
        self.logger.setLevel(logging.INFO)
        # create file handler which logs even debug messages
        fh = logging.FileHandler('searcher.log')
        fh.setLevel(logging.INFO)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def run(self):
        while(True):
            commit_flag = [False,]
            try:
                
                git_folder = self.thread_pool.get_git_search_folder()
                git_folder_str = git_folder[1]
                os.chdir(constants.REPOSITORY_FOLDER+git_folder_str)
                self.__replace_dest_with_certain(constants.REPOSITORY_FOLDER+git_folder,
                                                constants.PATTEN,
                                                constants.REPLACEMENT,
                                                commit_flag)
                if(commit_flag[0] == True):
                    self.thread_pool.put_git_commit(git_folder)
                    self.logger.info(git_folder_str)
                    commit_flag[0] = False
            except Exception as e:
                print e

                print "things are wrong in searcher process"
                self.thread_pool.put_git_search_folder(git_folder)
                commit_flag[0] = False
            if self.thread_pool.git_search_folder.qsize() <= 0:
                time.sleep(20)
                if self.thread_pool.git_search_folder.qsize() <= 0:
                    break

    def _replace_dest_with_certain(self,path = None, patten = None,repl = None,commit_flag = None):
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
                            if(commit_flag[0] == False):
                                commit_flag[0] = True
                            print(file_path) 
                    except Exception :
                        print("failure path:"+file_path)

                    
                
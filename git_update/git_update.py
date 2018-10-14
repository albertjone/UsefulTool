import os
from git import Repo
import threading
import Queue
import time



class GitPuller(threading.Thread):
    def __init__(self,q,name):
        super(GitPuller, self).__init__()
        self.q = q
        self.start_flag = True
        self.naem = name

    def run(self):
        while self.start_flag:
            if self.q.empty():
                break
            repo_path = self.q.get(block=True,timeout=2)
            print(self.name + "start pull:" + repo_path)
            self.git_pull(repo_path)
            print(self.name + "fininsh pull" + repo_path)
            
    def git_pull(self,repo_path):
        repo = Repo(repo_path)
        origin = repo.remotes.origin
        origin.pull()
    
    def stop(self):
        if(self.start_flag == True):
            self.start_flag = False


def get_repo_paths(rep_path):
    print(os.listdir(rep_path))
    repo_path_list = os.listdir(rep_path)
    return repo_path_list 

    

def main():
    q = Queue.Queue()
    path = u"/Users/robot/Desktop/Openstack/Rep/"
    git_pullers = []
    repo_path_list = get_repo_paths(path)

    for repo in repo_path_list:
        q.put(path+repo,block=True,timeout=2)
    for i in range(0,100):
        git_pullers.append(GitPuller(q=q,name=i))
    start_time = time.time()
    print("start at:" + str(start_time))
    for puller in git_pullers:
        puller.start()
    finish_time = time.time()
    print("end at:" + str(finish_time))
    print("total coast" + str(finish_time -start_time))
    

if __name__ == "__main__":
    main()

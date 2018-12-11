import os
import threading
from git import Repo
import re
from utils import log
import time


L = threading.Lock()
taget_pattern = r'author-email = openstack-dev@lists.openstack.org'
replace_pattern = r'author-email = openstack-discuss@lists.openstack.org'
message = '\nChange openstack-dev to openstack-discuss \n\n\
Mailinglists have been updated. Openstack-discuss replaces\n\
openstack-dev.\n'
repo_path = '/home/guanalbertjone/rep'

#find the target and replace return Boolean
def find_replace(dirr):
    allfiles = []

    def dir_list(path, allfiles):
        file_list = os.listdir(path)
        for file_name in file_list:
            file_path = os.path.join(path, file_name)
            if os.path.isdir(file_name):
                dir_list(file_name, allfiles)
            else:
                allfiles.append(file_path)
        return allfiles

    found = False
    for f in [file for file in dir_list(dirr, allfiles) 
              if os.path.isfile(file)]:
        content = ""
        fr = open(f, 'r')
        for line in fr.readlines():
            if re.search(taget_pattern, line):
                line = re.sub(taget_pattern,
                              replace_pattern,
                              line)
                found = True
            content += line
        if found:
            fw = open(f, 'w')
            fw.write(content)
            fw.close()
        print found
        fr.close()
    return found


def add_and_commit(dirr):
    repo = Repo(dirr)
    git = repo.git
    git.add('.')
    git.commit('-m', message)
    git.review()


def work(dirs):
    for d in dirs:
        if find_replace(d):
            time.sleep('20')
            add_and_commit(d)
            log(d)


def main():
    dirs = [os.path.join(repo_path, path) for path in os.listdir(repo_path)]
    ts = []
    work(dirs)



if __name__ == '__main__':
    main()

repo = Repo('/Users/robot/code/Openstack/Test/octavia-tempest-plugin')
git = repo.git
import pdb; pdb.set_trace()
if git.diff('--cached') or git.diff():
    
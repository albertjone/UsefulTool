import os
import threading
from git import Repo
import re
from utils import log


L = threading.Lock()
taget_pattern = r'author-email = openstack-dev@lists.openstack.org'
replace_pattern = r'author-email = openstack-discuss@lists.openstack.org'
message = '\nChange openstack-dev to openstack-discuss \n\n\
Mailinglists have been updated. Openstack-discuss replaces\n\
openstack-dev.'
repo_path = '/Users/robot/code/Openstack/Test'

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
    L.acquire()
    dirr = dirs.pop()
    L.release()
    if find_replace(dirr):
        add_and_commit(dirr)
        log(dirr)


def main():
    dirs = [os.path.join(repo_path, path) for path in os.listdir(repo_path)]
    ts = []
    for num in range(0, 2):
        ts.append(threading.Thread(target=work, args=(dirs,)))
    for t in ts:
        t.start()
    for t in ts:
        t.join()


if __name__ == '__main__':
    main()





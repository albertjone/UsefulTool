#!/usr/bin/env python
import os
import git
import threading
from time import ctime

L = threading.Lock()
direcotry = '/Users/robot/code/Openstack/Rep/'


def git_pull(paths):
    L.acquire()
    for path in paths:
        print('pulling .....', path)
        g = git.cmd.Git(path)
        g.pull()
    L.release()


def main():
    print('### start time:', ctime())
    paths = [os.path.join(direcotry, dir) for dir in os.listdir(direcotry)]
    threads = []
    for num in range(0, 99):
        t = threading.Thread(target=git_pull, args=(paths,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('### end time', ctime())


if __name__ == "__main__":
    main()

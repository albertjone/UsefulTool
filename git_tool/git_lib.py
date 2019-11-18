from git import Repo

from common import utils
from common.exceptions import DirectoryExists
from common import logs

from multiprocessing import Process
from urllib.parse import urljoin

HTTPS = 'https'
GIT = 'git'

def git_clone_repo_from(url, to_path):
    logs.log_repo_start_to_clone(url, to_path)
    if utils.dir_already_existed(to_path):
        if not Repo(to_path).bare:
            return
    Repo.clone_from(url, to_path)


def git_clone_repos_from(repo_args):
    pool = []
    for arg in repo_args:
        p = Process(target=git_clone_repo_from, args=arg)
        pool.append(p)
    for p in pool:
        p.start()
        p.join()


def get_repo_url(repo_base, name):
    if not repo_base.endswith('/'):
        repo_base = repo_base + '/'
    if repo_base.startswith(HTTPS):
        name = name + '.git'
        repo_url = urljoin(repo_base, name)
    else:
        repo_url = urljoin(repo_base, name)
    return repo_url


def get_repo_path(path_base, name):
    repo_path = urljoin(path_base, name)
    return repo_path

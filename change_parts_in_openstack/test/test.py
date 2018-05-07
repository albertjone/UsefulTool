import Queue

queue = Queue.Queue()
queue.put(1)
queue.put(1)
queue.put(1)
print queue.qsize()
# if 1 in queue:
#     print "1 is in the queue"


# import os
# # from change_parts_in_openstack import constants
# import commands
# # result = os.listdir(constants.REPOSITORY_FOLDER)
# # print result
# os.chdir("/home/openstack/Desktop/Openstack/performance-docs")

# print os.getcwd()
# results = commands.getoutput("grep -n -r 'https://pypi.python.org/pypi/'").split("  ")
# print results

# # print results
# for item in results:
#     print item
# print os.path.abspath('..')


# print os.listdir(os.getcwd())


# path =  os.path.join("/root","requirements.txt")
# print path


# import os 
# import git
# from git import Repo

# def print_repository(repo):
#     print('Repo description: {}'.format(repo.description))
#     print('Repo active branch is {}'.format(repo.active_branch))
#     for remote in repo.remotes:
#         print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
#     print('Last commit for repo is {}.'.format(str(repo.head.commit.hexsha)))

# def print_commit(commit):
#     print('----')
#     print(str(commit.hexsha))
#     print("\"{}\" by {} ({})".format(commit.summary,
#                                      commit.author.name,
#                                      commit.author.email))
#     print(str(commit.authored_datetime))
#     print(str("count: {} and size: {}".format(commit.count(),
#                                               commit.size)))

# if __name__ == "__main__":
#     repo_path = "/home/openstack/Desktop/fsp"
#     # Repo object used to programmatically interact with Git repositories
#     repo = Repo(repo_path)
#     # check that the repository loaded correctly
#     if not repo.bare:
#         print('Repo at {} successfully loaded.'.format(repo_path))
#         print_repository(repo)
#         # create list of commits then print some of them to stdout
#         commits = list(repo.iter_commits('master'))
#         for commit in commits:
#             print_commit(commit)
#             pass
#     else:
#         print('Could not load repository at {} :('.format(repo_path))



# import os 
# import git
# import constants
# os.chdir("/home/openstack/Desktop/Openstack/performance-docs")
# print("in commit progress")
# print(os.getcwd())
# os.system("git add .")
# os.system('git commit --message="Trivial: Update pypi url to new url"')
# os.system('git review')



import commands
print "command test"
print commands.getstatusoutput("/home/mrrobot/Desktop/Openstack/python-novaclient")
print commands.getstatusoutput("git add .")
print commands.getstatusoutput("git commit --message 'this is test'")
print commands.getstatusoutput("git review")
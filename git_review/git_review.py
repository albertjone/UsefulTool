from git import Repo
from git import osp

repo = Repo("/Users/mrrobot/Desktop/Openstack/nova")
# nova = repo.clone(path="https://github.com/openstack/nova.git")
# assert repo.__class__ is Repo

# develop = repo.create_head('test')
# assert develop == repo.active_branch
# print develop.commit.message
# develop.checkout()
# open('/Users/mrrobot/Desktop/Openstack/nova/test.txt','wr').close()
# repo.index.commit("add a new file test.txt")
new_branch = repo.create_head('new')     # create a new one
new_branch.commit = 'HEAD~10'            # set branch to another commit without changing index or working trees
repo.delete_head(new_branch)             # delete an existing head - only works if it is not checked out
from git import Git
from git import Repo
import os
import commands
from threading import Lock

reps_path = '/root/reps/'
reps = os.listdir(reps_path)
lock = Lock()
t_name = '.gitignore'
message = """
since vscode is commonly used in our development progress and will create\n
.vscode folder which make us not convenient to git add with the .gitignore\n
now. So it is necessary to update the .gitignore file.
"""

def target():
    while True:
        with lock:
            rep = reps.pop()
        if not rep:
            continue
        if not os.path.isdir():
            continue
        rep_path = reps_path + rep
        t_file = commands.getoutput('find ' + rep_path + ' -name .gitignore')
        f = open(t_file, 'a')
        f.write('\n # vscode staff\n.vscode')
        f.close()
        try:
            os.system('cd ' + rep_path)
            os.system('git add . ')
            os.system('git commit -m ' + message)
            os.system('git review')
        except Exception as e:
            print e





def main():
    pass

if __name__ == "__main__":
    main()


from git import Git
from git import Repo
import os
import commands

message = """
since vscode is commonly used in our development progress and will create
.vscode folder which make us not convenient to git add with the .gitignore
now. So it is necessary to update the .gitignore file.
"""
message = """
since vscode is commonly used in our development progress and will create\n
.vscode folder which make us not convenient to git add with the .gitignore\n
now. So it is necessary to update the .gitignore file.
"""


def test():
    rep_path = '/root/reps/nova/nova'
    t_file = commands.getoutput('find ' + rep_path + ' -name .gitignore')
    f = open(t_file, 'a')
    f.write('\n # vscode staff\n.vscode')
    f.close()
    try:
        os.system('cd ' + rep_path)
        os.system('git add . ')
        os.system('git commit -m ' + message)
        os.system('git review')
    except Exception as e:
        print e
test()
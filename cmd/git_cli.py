import argparse 
from common import utils
from git_tool import git_lib

parser = argparse.ArgumentParser(description='Process git command options')
parser.add_argument('action',
                    help='only clone, pull, push can be added'
                    'clone repositories you set at from your config file'
                    'pull repositories you set at from your config file'
                    'push repositories you set at from your config file',
                    choices=['clone', 'pull', 'push'],
                    nargs=1
                    )
parser.add_argument('--reps_file', default='./repos_file.yaml',
                    help='config file for target repositories'
                    )

CLONE = 'clone'
PULL = 'pull'
PUSH = 'push'


def main():
    args = parser.parse_args()
    action = args.action[0]
    file_name = args.reps_file
    content = utils.parse_from_yaml_file_str(file_name)
    base_url = content['repo_base']['location']
    names = content['repo_base']['repo_names']
    base_path = content['dest_dir']
    repo_args = [(git_lib.get_repo_url(base_url, name),
                  git_lib.get_repo_path(base_path, name)) for name in names]
    if action == CLONE:
        git_lib.git_clone_repos_from(repo_args)


if __name__ == "__main__":
    main()

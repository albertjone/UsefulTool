SPIDER_COUNT = 4
GITCLONER_COUNT = 4
UPDATER_COUNT = 4
SEARCHER_COUNT = 4
COMMITER_COUNT = 4


#Spider
START_URL = "https://github.com/openstack"
SPIDER_WAIT = 3

#GitClone
REPOSITORY_FOLDER = "/home/openstack/Desktop/OpenstackTest/"
# REPOSITORY_FOLDER = "/home/mrrobot/Desktop/Openstack"


#Search
SEARCH_WAIT = 3
PATTEN = ""
REPLACEMENT = ""
FILE_TYPE = ['gif','png','bmp','jpg','jpeg','rar','zip',
            'ico','apk','ipa','doc','docx','xls','jar',
            'xlsx','ppt','pptx','pdf','gz','pyc','class']
#Commit
COMMIT_WAIT = 3
COMMIT_MESSAGE = "Trivial: Update pypi url to new url"
#  "Trivial: Update pypi url to new url"

#process S
CLONER_DELAY = 60
SEARCHER_DELAY = 120
COMMITER_DELAY = 120
UPDATER_DELAY = 7200


#log configuration
LOGPATH = '/home/openstack/UsefulTool/change_parts_in_openstack/logs'
notify = set()
notify.add(1)
notify.add(2)
notify.add(3)
notify.add("four")
notify.add("five")
notify.add(6)
b = set()
b.add(1)
print notify
res = notify - b
print "res"
print res
print notify
notify.clear()
print notify

import commands

cmd = "ls -lh"
result = commands.getoutput(cmd)
print "cmd result "
print result

import git
import os
if not os.path.isdir("/home/mrrobot/Desktop/Test"):
    os.mkdir("/home/mrrobot/Desktop/Test")
os.chdir("/home/mrrobot/Desktop/Test")
dirs = set(os.listdir("/home/mrrobot/Desktop"))
print dirs

import logging
import requests
import json
RELEASE_PATCH_URL = "https://review.openstack.org/changes/?q=project:openstack/releases+status:open&n=25&O=81"

PATCH_FILE = "%s/patch.json" % "/home/mrrobot/Desktop"
def _get_file(url, type):
    try:
        r = requests.get(url, timeout=10, headers={'Connection':'close'})
        with open(PATCH_FILE, "wb") as code:
            code.write(r.content)
        os.system("sed -i '1d' %s" % PATCH_FILE)
    except:
        LOG.error("[search] get %s file failed ! url=%s" % (type, url))
        return {}
    with open(PATCH_FILE, 'r') as f:
        json_file = json.load(f)
    print "json_file"
    return json_file


    
for patch in _get_file(RELEASE_PATCH_URL,"patch")
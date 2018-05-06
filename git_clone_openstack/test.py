# from urllib import request
# url="https://github.com/openstack"
# req = request.Request(url=url)
# print(request.urlopen(url=url).read())

from downloader import Downloader
from mparser import MParser
from scheduler import Scheduler

import os
import git

# path = os.mkdir(name="C:\\Users\\Mr.Guan\\Desktop\\OpenstackREP\\")
# os.chdir(path="C:\\Users\\Mr.Guan\\Desktop\\OpenstackREP\\")
# print(os.getcwd())

# downloader = Downloader()
# parser = MParser()
# scheduler = Scheduler()
# content = downloader.download(url="https://github.com/openstack?page=2")
# if not content:
#     print("get content")
# urls, target_urls = parser.parse(content)
# print(urls)
# print(target_urls)


		
# path="/home/openstack/Desktop/Openstack"			
# git.Git(path).clone("https://github.com/openstack/kolla"+".git")	
		

# from multiprocessing import Process
# import os
# class Info(object):
#     def printName(self):
#         print"module name", __name__
# def info(title):
#     print title
#     print 'module name:', __name__
#     if hasattr(os, 'getppid'):  # only available on Unix
#         print 'parent process:', os.getppid()
#     print 'process id:', os.getpid()

# def f(name):
#     info('function f')
#     print 'hello', name

# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()
#     info = Info()
#     info.printName()


# from multiprocessing import Process, Lock
# nums = [1,2,3,4]
# def f(l):
#     l.acquire()
#     num = nums.pop()
#     print 'hello world', str(num)
#     l.release()

# if __name__ == '__main__':
#     lock = Lock()
    
#     for num in nums:
#         Process(target=f, args=(lock,)).start()


# import socket
# from concurrent import futures

# def blocking_way():
#     sock = socket.socket()
#     sock.connect(('example.com',80))
#     req = 'GET /HTTP/1.0 \r\nHost: example.com\r\n\r\n'
#     sock.send(req.encode('ascii'))
#     response = b''
#     chunk = sock.recv(4096)
#     while chunk:
#         response += chunk

#         chunk = sock.recv(4096)
#     return response

# def sync_way():
#     res = []
#     for i in range(10):
#         res.append(blocking_way())
#     return res

# def process_way():
#     workers = 10
#     with futures.ProcessPoolExecutor(workers) as excuter:
#         print(excuter.submit(blocking_way))
#         futs = {excuter.submit(blocking_way) for i in range(10)}
#     return [fut.result()for fut in futs]


# print type(process_way()[0])




# result = [lambda x: x + i for i in range(10)]
# print(result[0](10))
# print(len(result))



# import os
# from git import Repo
# url = os.getcwd()
# print url
# reps_url = "/home/openstack/Desktop/Openstack"
# # if url != "/home/mrrobot/Desktop/Openstack":
# if url != reps_url:    
#     os.chdir(reps_url)
#     print os.getcwd()
# repo_urls = os.listdir(os.getcwd())
# print("there are "+str(len(repo_urls))+" reps")
# repo = Repo(repo_urls[0])
# o = repo.remotes.origin 
# o.pull()
# # repo_urls = [repo_url for repo_url in os.listdir(os.getcwd()) if not Repo(repo_url).bare()]

# target_strs = [os.system('grep -rn "https://pypi.python.org/pypi" .')]
# print len(target_strs)


import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
import json


print os.getcwd()
PATCH_FILE = os.getcwd()+"/patch.json"
print PATCH_FILE
RPM_PACKAGING_PATCH_URL = "https://review.openstack.org/changes/?q=project:openstack/rpm-packaging+status:open&n=75&O=81"
r = requests.get(RPM_PACKAGING_PATCH_URL, timeout=10, headers={"Connection":"close"})
with open("%s" % PATCH_FILE, "wb") as code:
    code.write(r.content)
os.system("sed -i '1d' %s" % PATCH_FILE)


with open("%s" % PATCH_FILE, "r") as f:
    context = json.load(f)
len(context)

for obj in context:
    if cmp(obj.get("branch"), "master"):
        continue
    subject = obj.get("subject")
    if not subject:
        continue
    print subject
    lname = project_name.lower()
    _str = "%s "%lname
    if _str in subject.lower():
        print "this is true"

    
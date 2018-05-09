# -*- coding: utf-8 -*-


# target_url = "/home/mrrobot/Desktop/Openstack/python-novaclient/CONTRIBUTING.rst/bindep.txt"
# # data = open(target_url,'r').read()
# # print(data)
# # open(target_url).write(data)
# file1 = open('testfile.txt','w') 
 
# file1.write('Hello World') 
# file1.write('This is our new text file') 

 
# file1.close() 
# with open(target_url,'r') as f:
#     print f.readline()


import commands

if(commands.getstatusoutput("cd /lo")[0] == 0):
    print "ok"
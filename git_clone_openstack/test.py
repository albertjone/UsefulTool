# from urllib import request
# url="https://github.com/openstack"
# req = request.Request(url=url)
# print(request.urlopen(url=url).read())

from downloader import Downloader
from mparser import MParser
from scheduler import Scheduler

import os



# path = os.mkdir(name="C:\\Users\\Mr.Guan\\Desktop\\OpenstackREP\\")
# os.chdir(path="C:\\Users\\Mr.Guan\\Desktop\\OpenstackREP\\")
# print(os.getcwd())

downloader = Downloader()
parser = MParser()
scheduler = Scheduler()
content = downloader.download(url="https://github.com/openstack?page=2")
if not content:
    print("get content")
urls, target_urls = parser.parse(content)
print(urls)
print(target_urls)


		
		
		
		
		
		





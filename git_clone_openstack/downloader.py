from urllib2 import request

class Downloader(object):

    def download(self, url):
        if url is None:
            return None
        req = request.Request(url=url)
        return request.urlopen(req).read()


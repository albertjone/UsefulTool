from urllib import request,error

class Downloader(object):

    def download(self, url):
        if url is None:
            return None
        req = request.Request(url=url)
        return req.urlopen(req).read()


import urllib2


class Downloader(object):

    def download(self, url):
        return urllib2.urlopen(url=url).read()

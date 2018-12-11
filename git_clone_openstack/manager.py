import os
import git
import setting

from scheduler import Scheduler
from downloader import Downloader
from mparser import MParser
from oslo_config import cfg
from oslo_log import log as logging


LOG = logging.getLogger(__name__)
CONF = cfg.CONF
DOMAIN = 'manager'


logging.register_options(CONF)
logging.setup(CONF, DOMAIN)


class Manager(object):
    def __init__(self, start_url=None):
        self.parser = MParser()
        self.downloader = Downloader()
        self.scheduler = Scheduler()
        self.target_urls = list()
        self.start_url = start_url
        self.page = 1
        self._init_processes()

    def _init_processes(self):
        self.mparsers = [MParser() for i in range(setting.MPARSER_NUM)]
        self.downloaders = \
            [Downloader() for i in range(setting.DOWNLOADER_NUM)]
        self.schedulers = \
            [Scheduler() for i in range(setting.SCHEDULER_NUM)]

        self.scheduler.add_new_url(self.start_url)
        # while self.scheduler.has_url():
        count = 1
        while count <= 57:
            url = self.scheduler.get_url()
            print("get page" + str(self.page) + ":" + url)
            if not url:
                self.page += 1
            try:
                content = self.downloader.download(url)
                urls, target_urls = self.parser.parse(content)
                for url in urls:
                    self.scheduler.add_new_url(url)
                for url in target_urls:
                    self.target_urls.append(url)
                count += 1
                for url in self.target_urls:
                    try:
                        gitclone(url)
                    except Exception as e:
                        print(e)
            except Exception as e:
                print("get total" + str(count) + "pages")
        print("get total:" + str(len(self.target_urls)))
        print(self.target_urls[6])


def gitclone(url):
    if not os.path.isdir(url):
        print("current download git is:" + url)
        git.Git(setting.linux_path).clone(url + ".git")
    else:
        print("skip url is :" + url)


def main():
    if os.name == "posix":
        LOG.info('your system is posix')
        path = setting.linux_path
        if not os.path.isdir(path):
            LOG.info('begin to create repository folder')
            path = os.mkdir(path)
            LOG.info("repository folder is created")
            os.chdir(path)
            print("current folder is :" + os.path.curdir())
        else:
            print("the destination exits")
            os.chdir(path)
    else:
        print("your current system is windowshood")
        path = setting.win_path
        if not os.path.isdir():
            print("begin to create repository ")
            path = os.mkdir(path)
            print("repository is created")
            os.chdir(path)
            print("current folder is :" + os.path.curdir())
        else:
            os.chdir(path)
print("repository created")
    manager = Manager("https://github.com/openstack")
    target_urls = manager.run()


if __name__ == "__main__":
    main()







class Scheduler():
    def __init__(self):
        self.url_list = list()
        self.out_count = 0
        self.max_count = 0

    def add_new_url(self, url):
        if url not in self.url_list:
            self.url_list.append(url)
            self.max_count = len(self.url_list)+1

    def has_url(self):
        if self.out_count >= self.max_count:
            return False
        else:
            return True

    def get_url(self):
        url = self.url_list[self.out_count]
        self.out_count +=1
        print("current url in get_url of scheduler is "+str(type(url)))
        print(url)
        return url


    
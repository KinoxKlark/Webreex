from abc import ABC, abstractmethod

class WalkerException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class Walker(ABC):
    """A Walker object browse a website and extracts the maximum of page hi can"""

    def __init__(self, config):

        self.urls = []
        self.config = {
            'mask': '',         # The mask for validating an url
            'max_depth': 50,    # The maximum depth in wich the walker search a page
        }.update(config)
        self.depth = 0

    def __setattr__(self, name, value):
        if name == 'config':
            self.config.update(value)
        object.__setattr__(self, name,value)

    def setConfig(self, config):
        """Override the config of the walker

        :param config A configuration dictionary"""
        self.config.update(config)

    def startWalk(self, start_url):
        """Start walking from here"""
        if (not self.addUrl(start_url)):
            raise WalkerException('The starting url is invalid. Does it match the mask ?')
        self.walk()

    @abstractmethod
    def walk(self):
        """Walk around while ther is pages or while above max depth"""
        pass

    def walkTo(self, url):
        """Walk to a specific url, manipule the page and get all nexts urls

        :return boolean True if the page existe and false if there is a problem"""
        # todo use PageManager to save a page and get next urls back
        # 1) call page manger manager.feed(url)
        # 2) get new url lists and merge
        # 3) catch exception
        # 4) manage depth
        pass

    def addUrls(self, urls = []):
        """Add multiple urls to the list"""
        for url in urls:
            self.addUrl(url)

    def addUrl(self, url):
        """Add a url to the list
        :param url The url to add to the list
        :return boolean true if the url has been added"""
        if (url not in self.urls) and self.urlIsValid(url):
            self.urls.append(url)
            return True
        return False

    def removeUrls(self, urls = []):
        """Remove multiple urls from the list"""
        for url in urls:
            self.removeUrl(url)

    def removeUrl(self, url):
        """Eemove a url from the list"""
        try:
            del self.urls[self.urls.index(url)]
        except ValueError as err:
            pass

    def urlIsValid(self, url):
        mask = self.config['mask']
        # todo check mask
        return True
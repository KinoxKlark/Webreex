# import TreeNode as node

class Walker():
    """
    A Walker object browse a website and extracts the maximum number of page hi can
    """

    def __init__(self, start_url: str, max_depth=10, masks=['*']):
        """
        Construct a Walker

        :param start_url    The url from which we will start the walk
        :param max_depth    The maximum depth at which to retrieve a page from the starting URL
        :param masks        A list of masks we will apply on each url to check if we should retrieve the page or not
        """

        # Private
        self._current_depth = 0
        self._urls = []
        self._tree_node_root = None
        self._tree_node_current = None

        # Public
        self.start_url = start_url
        self.masks = masks
        self.max_depth = max_depth

    def walk_through(self):
        """
        Start walking from start_url to all pages that correspond to a mask and that are not too far from start_url
        """
        if not self._add_url(self.start_url):
            raise WalkerException('The starting url is invalid. Does it match any mask ?')
        self._walk()

    def _walk(self):
        """Walk recursively in all possible pages"""
        i = 0
        while i < len(self._urls) and self._current_depth <= self.max_depth:
            if self._walk_to(self._urls[i]):
                i += 1

    def _walk_to(self, url):
        """
        Walk to a specific url, manipule the page and get all nexts urls
        :return boolean True if the page existe and false if there is a problem
        """
        # todo use PageManager to save a page and get next urls back
        # 1) call page manger manager.feed(url)
        # 2) get new url lists and merge
        # 3) catch exception
        # 4) manage depth
        pass

    def _add_url(self, url):
        """
        Add a url to the list
        :param url The url to add to the list
        :return boolean true if the url has been added
        """
        if (url not in self._urls) and self._url_is_valid(url):
            self._urls.append(url)
            return True
        return False

    def _url_is_valid(self, url):
        """
        Check if an url is valid by checking if it corespond to a mask
        :param url:
        :return boolean:
        """
        for mask in self.masks:
            pass  # todo check mask
        return True


class WalkerException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

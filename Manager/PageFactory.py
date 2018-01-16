class PageFactory:
    __collection = {}
    __parser = None
    __data_source = None

    def __init__(self):
        pass

    def get_page(self, url):
        if self.__collection[url] is not None:
            return self.__collection[url]

    def __get_hash(self, url):
        pass

    def __init_data_source(self):
        pass

    def __init_parser(self):
        pass

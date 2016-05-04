class PageBase(object):

    def __init__(self, browser):
        self._browser = browser
        self.url = ''

    @property
    def get_browser(self):
        return self._browser

    def get_url(self):
        self.get_browser.get(self.url)
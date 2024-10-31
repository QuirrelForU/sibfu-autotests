class ExamplePage:
    URL = "https://example.com"
    TITLE = "Example Domain"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def get_title(self):
        return self.page.title()

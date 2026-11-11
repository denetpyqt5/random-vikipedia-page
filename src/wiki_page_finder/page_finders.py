import pywikibot

class WikipediaParser:
    def __init__(self):
        site = pywikibot.Site("ru", "wikipedia")
        self.random_pages = site.randompages(total=1, namespaces=0)

    def get_random_page(self):
        for page in self.random_pages:
            print(page.title(), page.full_url())
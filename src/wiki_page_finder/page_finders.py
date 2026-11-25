import time
import webbrowser

import pywikibot

pywikibot.config.base_dir = (
    r"C:\Users\aieng\OneDrive\Desktop\random-vikipedia-page\config"
)


class WikipediaParser:
    def __init__(self, lang="ru"):
        self.site = pywikibot.Site(lang, "wikipedia")

    def get_random_pages(self, count: int):
        return list(self.site.randompages(total=count, namespaces=0))

    @staticmethod
    def get_pages_info(pages):
        for page in pages:
            time.sleep(5)
            categories = list(page.categories())
            titles = [x.title() for x in categories]
            print(page.title(), page.full_url())
            for title in titles:
                print(title)

    @staticmethod
    def open_url(pages):
        for page in pages:
            webbrowser.open(page.full_url())

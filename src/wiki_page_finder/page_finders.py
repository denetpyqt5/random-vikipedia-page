import pywikibot
import webbrowser

pywikibot.config.base_dir = (
    r"C:\Users\aieng\OneDrive\Desktop\random-vikipedia-page\config"
)


class WikipediaParser:
    def __init__(self):
        site = pywikibot.Site("ru", "wikipedia")
        self.random_pages = list(site.randompages(total=1, namespaces=0))

    def get_random_page(self):
        for page in self.random_pages:
            print(page.title(), page.full_url())

    def open_url(self):
        for page in self.random_pages:
            webbrowser.open(page.full_url())
import pywikibot

site = pywikibot.Site("ru", "wikipedia")

random_pages = site.randompages(total=1,namespaces=0)

for page in random_pages:
    print(page.title(),page.full_url())
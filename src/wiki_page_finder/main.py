from page_finders import WikipediaParser

if __name__ == "__main__":
    parser = WikipediaParser()
    pages = parser.get_random_pages(5)
    parser.get_pages_info(pages)

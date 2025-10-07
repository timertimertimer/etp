from scrapy.cmdline import execute


def akosta_bankruptcy():
    execute(["scrapy", "crawl", "akosta_bankruptcy"])


def akosta_arrested():
    execute(["scrapy", "crawl", "akosta_arrested"])


def akosta_commercial():
    execute(["scrapy", "crawl", "akosta_commercial"])


if __name__ == "__main__":
    akosta_bankruptcy()

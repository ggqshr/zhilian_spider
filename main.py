from scrapy.cmdline import execute
from zhilian.settings import AIM_DATE
import sys
import os



sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
   # if not AIM_DATE:
       # execute(["scrapy", "crawl", "zl_all"])
    #else:
    execute(["scrapy", "crawl", "zl_complete"])


if __name__ == "__main__":
    main()
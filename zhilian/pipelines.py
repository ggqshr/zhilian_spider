# -*- coding: utf-8 -*-
import pymongo
from scrapy.exceptions import DropItem
from zhilian.items import ZhilianItem, XiaozhaoItem

class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db, mongo_collection_soc, mongo_collection_camp):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection_soc = mongo_collection_soc
        self.mongo_collection_camp = mongo_collection_camp

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE'),
            mongo_collection_soc=crawler.settings.get('MONGO_COLLECTION_SOC'),
            mongo_collection_camp=crawler.settings.get('MONGO_COLLECTION_CAMP')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()
        from datetime import datetime
        with open("result.log", "a") as f:
            f.writelines("{} crawl item {} \n".format(datetime.now().strftime("%Y.%m.%d"), self.count))
            f.flush()

    def process_item(self, item, spider):
        try:
            if isinstance(item, ZhilianItem):
                # self.db[self.mongo_collection].update({'link': item['link']}, {'$set': dict(item)}, True)
                self.db[self.mongo_collection_soc].insert(item)
            else:
                self.db[self.mongo_collection_camp].insert(item)
            return item
        except pymongo.errors.DuplicateKeyError:
            raise DropItem("Drop duplicate item %s" % item)

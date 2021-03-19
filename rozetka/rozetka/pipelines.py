# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os 
from scrapy.pipelines.images import ImagesPipeline

class MyImagesPipeline(ImagesPipeline):
    count = 0 
    def file_path(self, request, response=None, info=None, *, item=None):
        self.count += 1
        return f"name{self.count}.jpg"


class RozetkaPipeline:
    def process_item(self, item, spider):
        if spider.name == "laptop":
            print("="*50)
            print (item["files"][0]["path"].split("/")[-1])
        return item

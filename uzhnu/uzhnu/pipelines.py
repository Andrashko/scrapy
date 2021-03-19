from itemadapter import ItemAdapter
from sqlite3 import connect 
from scrapy.exceptions import DropItem


class UzhnuPipeline:

    def open_spider(self, spider):
        self.number=0

    def process_item(self, item, spider):
        item["processed"] = True
        self.number += 1
        item["number"] = self.number
        return item

    def close_spider(self, spider):
        print("="*50)
        print(f"{self.number} items have been processed")


class SqlitePipeline:
    
    def __init__(self, file_name):
        self.file_name = file_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(file_name=crawler.settings.get("DB_FILE_NAME"))

    def open_spider(self, spider):
        self.connection = connect(self.file_name)

    def process_item(self, item, spider):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO faculty (name, url, processed, number) VALUES (?, ?, ?, ?)", [item["name"], item["url"], item ["processed"], item["number"]])
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.connection.close()


class DuplicatFilterPipeline:

    def __init__(self, file_name):
        self.file_name = file_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(file_name=crawler.settings.get("DB_FILE_NAME"))

    def open_spider(self, spider):
        self.connection = connect(self.file_name)

    def process_item(self, item, spider):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM faculty WHERE url = ?", [item["url"]])
        if cursor.fetchone()[0] > 0:
            raise DropItem(f"Duplicate {item['url']}")        
        return item

    def close_spider(self, spider):
        self.connection.close()

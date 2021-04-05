from itemadapter import ItemAdapter
import sqlite3
from db.items import FacultyItem, DepartmetItem

class SaveFacultyToDBPipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect("uzhnudb.db")
        cursor = self.connection.cursor()
        self.facuty_set = set()
        for name in cursor.execute("SELECT name FROM faculty"):
            self.facuty_set.add(name[0])
        print(self.facuty_set)

    def process_item(self, item, spider):
        if isinstance(item, FacultyItem):
            cursor = self.connection.cursor()
            if not item["name"] in self.facuty_set:
                cursor.execute("INSERT INTO faculty (Name, Url) VALUES (?,?)", [item["name"], item["url"]])
                self.facuty_set.add(item["name"])
            self.connection.commit()
        return item
    
    def close_spider(self, spider):
        self.connection.close()


class SaveDepartmentToDBPipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect("uzhnudb.db")
        cursor = self.connection.cursor()
        self.department_set = set()
        for name in cursor.execute("SELECT name FROM department"):
            self.department_set.add(name[0])

    def process_item(self, item, spider):
        if isinstance(item, DepartmetItem):
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT Id FROM faculty WHERE name = \"{item['faculty']['name']}\"")
            item["faculty_id"] = cursor.fetchone()[0]
            if not item["name"] in self.department_set:
                cursor.execute("INSERT INTO department (Name, Url, FacultyId) VALUES (?,?, ?)", [item["name"], item["url"],item["faculty_id"]])
                self.department_set.add(item["name"])
        self.connection.commit()
        return item
    
    def close_spider(self, spider):
        self.connection.close()

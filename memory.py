import json
import tinydb
from tinydb import Query

MEMORY_FILE = "filings.json"

class FilingsMemory():
    def __init__(self):
        self.db = tinydb.TinyDB(MEMORY_FILE)
    
    def insert_one(self, filings_dict):
        self.db.insert(
                filings_dict
            )

    def insert(self, batch):
        if type(batch) == list:
            self.db.insert_multiple(batch)
        
        else:
            self.db.insert(batch)
        


    def find_one(self, filing):
        filings = Query()

        result = self.db.search(
            (filings.filename == filing.get("filename")) & 
            (filings.entity_name == filing.get("entity_name")) &
            (filings.date == filing.get("date"))
        )

        return result


    def exists(self, filing):
        result = self.find_one(filing)

        return len(result) > 0 

import json
import tinydb
from tinydb import Query


class Memory():
    
    def __init__(self):
        self.db = tinydb.TinyDB("memory.json")
    
    def save_memory(self, values_dict):
        for value in values_dict :
            db.insert(
                value
            )


    def load_memory(self):
        return db.all()

    def exists(self, value_dict):
        filings = Query()

        result = db.search(
            filings.date == value_dict.get("date") and 
            filings.filename == value_dict.get("filename") and 
            filings.entity_name == value_dict.get("entity_name")
        )

        return len(result) > 0 


    last_fetch_edgar(1)
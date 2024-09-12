from pymongo import MongoClient
from app.config.config import settings

class MongoDB:
    def __init__(self):
        self.client = MongoClient(settings.DB_URL)
        self.db = self.client[settings.DB_NAME]

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

# Initialize MongoDB connection
mongo_db = MongoDB()
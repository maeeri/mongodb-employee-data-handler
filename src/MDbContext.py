from pymongo import MongoClient
from dotenv import dotenv_values
from bson.objectid import ObjectId

config = dotenv_values()

class MongoDbDataHandler:
    def get_database(self):
        CONNECTION_STRING = config["MONGO_CONNECTION"]
        DBNAME = config["MONGO_DBNAME"]
        client = MongoClient(CONNECTION_STRING)
        return client[DBNAME]


    def clear_collection(self, collection: str):
        self.get_database().drop_collection(collection)


    def insert_collection(self, collection: str, items):
        db = self.get_database()
        coll = db.get_collection(collection)
        if coll is not None:
            coll.insert_many(items)
        else:
            db.create_collection(collection).insert_many(items)


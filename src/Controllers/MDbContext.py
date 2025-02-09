from pymongo import MongoClient
from bson import ObjectId


class MongoDbDataHandler:
    collection: str
    connectionString: str
    databaseName: str

    def __init__(self, dbName, collectionName, connectionString):
        self.databaseName = dbName
        self.collection = collectionName
        self.connectionString = connectionString

    def get_database(self):
        client = MongoClient(self.connectionString)
        return client[self.databaseName]

    def drop_collection(self):
        self.get_database().drop_collection(self.collection)

    def empty_collection(self):
        self.get_database().get_collection(self.collection).delete_many({})
        return self.get_all()

    def insert_collection(self, items):
        db = self.get_database()
        coll = db.get_collection(self.collection)
        if coll is not None:
            coll.insert_many(items)
        else:
            db.create_collection(self.collection).insert_many(items)

    def insert_one(self, item):
        db = self.get_database()
        coll = db.get_collection(self.collection)
        if coll is not None:
            return coll.insert_one(item).inserted_id
        else:
            return db.create_collection(self.collection).insert_one(item).inserted_id

    def get_all(self):
        output = []
        for item in self.get_database().get_collection(self.collection).find():
            output.append(self.id_helper(item))
        return output

    def get_one(self, id: id):
        return self.id_helper(
            self.get_database()
            .get_collection(self.collection)
            .find_one({"_id": ObjectId(id)})
        )

    def get_collection_count(self):
        return self.get_database().get_collection(self.collection).count_documents({})

    def id_helper(self, item: dict) -> dict:
        item["_id"] = str(item["_id"])
        return item

    def get_aggregate_result(self, pipeline: list):
        return (
            self.get_database()
            .get_collection(self.collection)
            .aggregate(pipeline)
            .to_list()
        )

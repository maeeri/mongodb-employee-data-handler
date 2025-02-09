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

    def get_all(self, collection: str):
        output = []
        for employee in self.get_database().get_collection(collection).find():
            output.append(self.employee_id_helper(employee))
        return output

    def employee_id_helper(self, employee) -> dict:
        return {
            "id": str(employee["_id"]),
            "gender": employee["gender"],
            "jobTitle": employee["jobTitle"],
            "educationLevel": employee["educationLevel"],
            "salary": employee["salary"],
            "age": employee["age"],
            "yearsOfExperience": employee["yearsOfExperience"],
        }

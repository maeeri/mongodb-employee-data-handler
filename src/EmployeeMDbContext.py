from src.MDbContext import MongoDbDataHandler
class EmployeeMongoDataHandler(MongoDbDataHandler):
    
    def __init__(self, dbName, connectionString):
        super().__init__(dbName, "employees", connectionString)


    def get_age_avg(self):
        pipeline = [
            {"$project": {"_id": 0, "gender": 1, "educationLevel": 1, "age": 1}},
            {
                "$match": {
                    "age": {"$not": {"$eq": 0}},
                    "educationLevel": {"$not": {"$eq": "N/A"}},
                },
            },
            {
                "$group": {
                    "_id": {"gender": "$gender", "educationLevel": "$educationLevel"},
                    "avg_age": {"$avg": "$age"},
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "educationLevel": "$_id.educationLevel",
                    "gender": "$_id.gender",
                    "avgAge": "$avg_age",
                }
            },
        ]
        return self.get_aggregate_result(pipeline)
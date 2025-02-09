from src.PGSQLContext import PGDataHandler
from src.MDbContext import MongoDbDataHandler
from dotenv import dotenv_values

config = dotenv_values()
mongoDbConnection = config["MONGO_CONNECTION"]
mongoDbDatabase = config["MONGO_DBNAME"]
collection = "employees"

if __name__ == "__main__":
    # pDb = PGDataHandler()
    # employees = pDb.get_all_employees()
    mongo = MongoDbDataHandler(mongoDbDatabase, collection, mongoDbConnection)
    print(mongo.get_all())

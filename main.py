from src.PGSQLContext import PGDataHandler
from src.EmployeeMdbContext import EmployeeMongoDataHandler
from dotenv import dotenv_values

config = dotenv_values()
mongoDbConnection = config["MONGO_CONNECTION"]
mongoDbDatabase = config["MONGO_DBNAME"]

if __name__ == "__main__":
    # pDb = PGDataHandler()
    # employees = pDb.get_all_employees()
    mongo = EmployeeMongoDataHandler(mongoDbDatabase, mongoDbConnection)
    print(mongo.get_age_avg())

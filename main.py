from src.PGSQLContext import PGDataHandler
from src.MDbContext import MongoDbDataHandler

collection = "employees"

if __name__ == "__main__":
    # pDb = PGDataHandler()
    # employees = pDb.get_all_employees()
    mDb = MongoDbDataHandler()
    print(mDb.get_all(collection))

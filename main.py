from src.PGSQLContext import PGDataHandler
from src.EmployeeMDbContext import EmployeeMongoDataHandler
from dotenv import dotenv_values
from fastapi import FastAPI, Response, APIRouter

config = dotenv_values()
mongoDbConnection = config["MONGO_CONNECTION"]
mongoDbDatabase = config["MONGO_DBNAME"]
mongo = EmployeeMongoDataHandler(mongoDbDatabase, mongoDbConnection)
pgsql = PGDataHandler()

app = FastAPI()
router = APIRouter(prefix="/api/v1")


@router.get("/")
async def health_check():
    return Response(content="{'status': 'success'}", status_code=200)

app.include_router(router)

# if __name__ == "__main__":
#     # pDb = PGDataHandler()
#     # employees = pDb.get_all_employees()
#     mongo = EmployeeMongoDataHandler(mongoDbDatabase, mongoDbConnection)
#     print(mongo.get_age_avg())
#     print(mongo.get_experience_max())
#     print(mongo.get_employee_count())
#     print(mongo.get_age_avg())
#     print(mongo.get_salary_sum())
#     print(mongo.get_employee_count_master())
#     print(mongo.get_max_salary_avg())

from src.PGSQLContext import PGDataHandler
from src.EmployeeMDbContext import EmployeeMongoDataHandler
from dotenv import dotenv_values
from fastapi import FastAPI, Response, APIRouter

config = dotenv_values()
mongoDbConnection = config["MONGO_CONNECTION"]
mongoDbDatabase = config["MONGO_DBNAME"]
mongo = EmployeeMongoDataHandler(mongoDbDatabase, mongoDbConnection)

app = FastAPI()
router = APIRouter(prefix="/api/v1")


@router.get("/")
async def health_check():
    return Response(content="{'status': 'success'}", status_code=200)


@router.get("/employees")
def employees():
    res = mongo.get_all()
    return res


@router.delete("/employees")
def delete_employees():
    try:
        mongo.empty_collection()
        return Response(content="{'delete': 'success'}", status_code=200)
    except:
        return Response(status_code=500)


@router.post("/employees/migrate")
def migrate_employees_from_pgsql_to_mongodb():
    try:
        if mongo.get_collection_count() > 0:
            return Response(
                content="{'info': 'The collection is not empty, no migration done'}"
            )
        else:
            pgsql = PGDataHandler()
            employees = pgsql.get_all_employees()
            mongo.insert_collection(employees)
            return Response(status_code=201)
    except:
        return Response(status_code=500)


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

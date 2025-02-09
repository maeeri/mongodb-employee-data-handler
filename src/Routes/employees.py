from src.Controllers.PGSQLContext import PGDataHandler
from src.Controllers.EmployeeMDbContext import EmployeeMongoDataHandler
from src.Models.EmployeeModel import RequestBodyEmployeeModel
from dotenv import dotenv_values
from fastapi import Response, APIRouter

config = dotenv_values()
mongoDbConnection = config["MONGO_CONNECTION"]
mongoDbDatabase = config["MONGO_DBNAME"]
mongo = EmployeeMongoDataHandler(mongoDbDatabase, mongoDbConnection)

employeesRoute = APIRouter(prefix="/api/v1/employees")


@employeesRoute.get("/")
def employees():
    res = mongo.get_all()
    return res


@employeesRoute.delete("/")
def delete_employees():
    try:
        mongo.empty_collection()
        return Response(content="{'delete': 'success'}", status_code=200)
    except:
        return Response(status_code=500)


@employeesRoute.post("/employee")
def insert_employee(employee: RequestBodyEmployeeModel):
    employeeJson = {
        "gender": employee.gender,
        "jobTitle": employee.jobTitle,
        "educationLevel": employee.educationLevel,
        "salary": employee.salary,
        "age": employee.age,
        "yearsOfExperience": employee.yearsOfExperience,
    }
    try:
        res = mongo.insert_one(employeeJson)
        return {"id": str(res)}
    except:
        return Response(status_code=500)


@employeesRoute.get("/employee/{id}")
def employee_by_id(id: str):
    try:
        return mongo.get_one(id)
    except Exception as e:
        print(e)


@employeesRoute.post("/migrate")
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


@employeesRoute.get("/salaries")
def average_salaries_by_gender_and_education_level():
    try:
        return mongo.get_salary_avg()
    except:
        return Response(status_code=500)


@employeesRoute.get("/experience")
def max_experience_by_gender_and_job_title():
    try:
        return mongo.get_experience_max()
    except:
        return Response(status_code=500)


@employeesRoute.get("/count")
def employee_count_by_job_title_and_education():
    try:
        return mongo.get_employee_count()
    except:
        return Response(status_code=500)


@employeesRoute.get("/ageavg")
def average_age_by_gender_and_education():
    try:
        return mongo.get_age_avg()
    except:
        return Response(status_code=500)


@employeesRoute.get("/salarysum")
def salaries_by_gender_and_job_title():
    try:
        return mongo.get_salary_sum()
    except:
        return Response(status_code=500)


@employeesRoute.get("/mastercount")
def employee_count_masters_degree_by_title_gte_15():
    try:
        return mongo.get_employee_count_master()
    except:
        return Response(status_code=500)


@employeesRoute.get("/maxavgsalary")
def highest_avg_salary_by_gender():
    try:
        return mongo.get_max_salary_avg()
    except:
        return Response(status_code=500)

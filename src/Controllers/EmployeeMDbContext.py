from src.Controllers.MDbContext import MongoDbDataHandler


class EmployeeMongoDataHandler(MongoDbDataHandler):

    def __init__(self, dbName, connectionString):
        super().__init__(dbName, "employees", connectionString)

    def get_salary_avg(self):
        pipeline = [
            {"$project": {"_id": 0, "jobTitle": 0, "yearsOfExperience": 0, "age": 0}},
            {"$match": {"educationLevel": {"$not": {"$eq": "N/A"}}}},
            {
                "$group": {
                    "_id": {"gender": "$gender", "educationLevel": "$educationLevel"},
                    "avg_salary": {"$avg": "$salary"},
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "gender": "$_id.gender",
                    "educationLevel": "$_id.educationLevel",
                    "avgSalary": "$avg_salary",
                }
            },
        ]
        return self.get_aggregate_result(pipeline)

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

    def get_experience_max(self):
        pipeline = [
            {
                "$project": {
                    "_id": 0,
                    "jobTitle": 1,
                    "gender": 1,
                    "yearsOfExperience": 1,
                }
            },
            {"$match": {"jobTitle": {"$not": {"$eq": "N/A"}}}},
            {
                "$group": {
                    "_id": {"gender": "$gender", "jobTitle": "$jobTitle"},
                    "max_experience": {"$max": "$yearsOfExperience"},
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "gender": "$_id.gender",
                    "jobTitle": "$_id.jobTitle",
                    "maxExperience": "$max_experience",
                }
            },
        ]
        return self.get_aggregate_result(pipeline)

    def get_employee_count(self):
        pipeline = [
            {"$project": {"_id": 0, "jobTitle": 1, "educationLevel": 1}},
            {
                "$match": {
                    "jobTitle": {"$not": {"$eq": "N/A"}},
                    "educationLevel": {"$not": {"$eq": "N/A"}},
                }
            },
            {
                "$group": {
                    "_id": {
                        "jobTitle": "$jobTitle",
                        "educationLevel": "$educationLevel",
                    },
                    "employee_count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "educationLevel": "$_id.educationLevel",
                    "jobTitle": "$_id.jobTitle",
                    "employeeCount": "$employee_count",
                }
            },
        ]
        return self.get_aggregate_result(pipeline)

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
                    "_id": {
                        "gender": "$gender",
                        "educationLevel": "$educationLevel",
                    },
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

    def get_salary_sum(self):
        pipeline = [
            {"$project": {"_id": 0, "gender": 1, "jobTitle": 1, "salary": 1}},
            {"$match": {"jobTitle": {"$not": {"$eq": "N/A"}}}},
            {
                "$group": {
                    "_id": {"gender": "$gender", "jobTitle": "$jobTitle"},
                    "salary_sum": {"$sum": "$salary"},
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "jobTitle": "$_id.jobTitle",
                    "gender": "$_id.gender",
                    "salarySum": "$salary_sum",
                }
            },
        ]
        return self.get_aggregate_result(pipeline)

    def get_employee_count_master(self):
        pipeline = [
            {
                "$project": {
                    "_id": 0,
                    "salary": 0,
                    "age": 0,
                    "yearsOfExperience": 0,
                    "gender": 0,
                }
            },
            {
                "$match": {
                    "educationLevel": "Master's Degree",
                    "jobTitle": {"$not": {"$eq": "N/A"}},
                }
            },
            {
                "$group": {
                    "_id": {"jobTitle": "$jobTitle"},
                    "employee_count": {"$sum": 1},
                }
            },
            {"$match": {"employee_count": {"$gte": 15}}},
            {
                "$project": {
                    "_id": 0,
                    "jobTitle": "$_id.jobTitle",
                    "employeeCount": "$employee_count",
                }
            },
        ]
        return self.get_aggregate_result(pipeline)

    def get_max_salary_avg(self):
        pipeline = [
            {"$project": {"_id": 0, "gender": 1, "salary": 1}},
            {"$match": {"gender": {"$not": {"$eq": "N/A"}}}},
            {
                "$group": {
                    "_id": {"gender": "$gender"},
                    "avg_salary": {"$avg": "$salary"},
                }
            },
            {"$sort": {"avg_salary": -1}},
            {"$limit": 1},
            {
                "$project": {
                    "_id": 0,
                    "gender": "$_id.gender",
                    "avgSalary": "$avg_salary",
                }
            },
        ]
        return self.get_aggregate_result(pipeline)

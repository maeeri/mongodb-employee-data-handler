import psycopg2
import contextlib
import dotenv

config = dotenv.dotenv_values()
print(config)


class PGDataHandler:

    @contextlib.contextmanager
    def connect(self):
        conn = None
        try:
            # replace with relevant info when testing
            conn = psycopg2.connect(
                database=(
                    config["POSTGRESQL_DB"]
                    if config["POSTGRESQL_DB"] != None
                    else "employeesdb"
                ),
                user=(
                    config["POSTGRESQL_USER"]
                    if config["POSTGRESQL_USER"] != None
                    else "app_user"
                ),
                password=(
                    config["POSTGRESQL_PWD"]
                    if config["POSTGRESQL_PWD"] != None
                    else "qwerty"
                ),
                host=(
                    config["POSTGRESQL_HOST"]
                    if config["POSTGRESQL_HOST"] != None
                    else "localhost"
                ),
                port=(
                    config["POSTGRESQL_PORT"]
                    if config["POSTGRESQL_PORT"] != None
                    else 5432
                ),
            )
            yield conn
        finally:
            if conn is not None:
                conn.close()

    def fetch_employees(self):
        qry = f"SELECT g.gender, jt.title, el.level, e.salary, e.age, e.years_of_experience \
                FROM employee e \
                JOIN education_level el ON e.education_level_id = el.id \
                JOIN gender g ON e.gender_id = g.id \
                JOIN job_title jt ON e.job_title_id = jt.id \
                ORDER BY g.gender, el.level;"
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute(qry)
            return cur.fetchall()

    def get_all_employees(self):
        res = self.fetch_employees()
        output = []
        for e in res:
            output.append(
                {
                    "gender": e[0],
                    "jobTitle": e[1],
                    "educationLevel": e[2],
                    "salary": e[3],
                    "age": e[4],
                    "yearsOfExperience": e[5],
                }
            )
        return output

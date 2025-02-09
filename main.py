from fastapi import FastAPI, Response
from src.Routes.employees import employeesRoute

app = FastAPI()


@app.get("/")
async def health_check():
    return Response(content="{'status': 'success'}", status_code=200)


app.include_router(employeesRoute)

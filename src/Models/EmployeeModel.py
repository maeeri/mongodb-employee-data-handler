from pydantic import BaseModel


class RequestBodyEmployeeModel(BaseModel):
    age: int
    gender: str
    educationLevel: str
    jobTitle: str
    yearsOfExperience: float
    salary: float

    def __init_subclass__(cls, **kwargs):
        return super().__init_subclass__(**kwargs)

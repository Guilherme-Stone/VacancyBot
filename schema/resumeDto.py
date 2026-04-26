from typing import Any
from pydantic import BaseModel

#user send data
class ResumeDtoCreate(BaseModel):
    city:str
    position:str
    salary_min:int
    salary_max:int
    country:str
    pass

#api return to the user
class ResumeDtoResponse(BaseModel):
    resume:list[str]
    pass

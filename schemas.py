from pydantic import BaseModel
from datetime import datetime

#Create Pydantic models for request and response
class BandCreate(BaseModel):
    specialization: str
    level: int
    status: str
    nickname: str
    contact: str
    date: str

class BandResponse(BandCreate):
    pass

class BankCreate(BaseModel):
    rate: int
    total_sum: int
    address: str
    security_rate: int
    name: str

class BankResponse(BankCreate):
    pass

class RobberyCreate(BaseModel):
    total_sum_for_each: int
    part: int
    date: datetime
    mark: int
    band_id: int
    bank_id: int

class RobberyResponse(RobberyCreate):
    pass


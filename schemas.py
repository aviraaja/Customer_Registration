from pydantic import BaseModel, EmailStr

class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str

class CustomerOut(CustomerCreate):
    id: int

    class Config:
        orm_mode = True



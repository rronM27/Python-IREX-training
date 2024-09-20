from pydantic import BaseModel, constr, conint, FieldValidationInfo, field_validator
from typing import Optional

class Address(BaseModel):
    street: str
    city: str


class User(BaseModel):
    id: conint(gt=0)
    name: constr(min_length=2, max_length=100)
    age: int
    @field_validator("age")
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("age must be positive")
        return v
    email: str
    address: Optional[str]=None


try:
    user1=User(id=0, name="John", age=0, email="user@gmail.com", address="123 Main Street")
    print(user1)
except Exception as e:
    print(e)

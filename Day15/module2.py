from fastapi import FastAPI
from pydantic import BaseModel, BaseSettings
from pydantic-settings import BaseSettings

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int

@app.post("/users/")
async def create_user(perdoruesi: User):
    return "ok. i have received the user name "+perdoruesi.name

#class Settings(BaseSettings):
#    app_name: str
#   admin_email: str
#    items_per_use: int=50
#
#settings = Settings("Fast api lesson", "admin@gmail.com")

@app.get("/users/")
async def create_user():
    return "Rron"

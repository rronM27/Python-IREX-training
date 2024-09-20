from fastapi import  FastAPI
from projekti1 import Developer, Project

app = FastAPI()

@app.post("/developers/")
async def create_developer(programeri: Developer):
    return {"message":"Developer created successfully",
            "developer":programeri}

@app.post("/projects/")
async def create_project(projekti: Project):
    return {"message":"Projekti created successfully",
            "Project":projekti}

@app.get("/projects/")
async def get_projects():
    Programeri=Developer(name="Dren")
    sample_project=Project(name="Sample Project",
                           description="This is a sample project",
                           language=["Python", "C++", "Java"],
                           lead_developer=Programeri)
    return{"projects": [sample_project]}
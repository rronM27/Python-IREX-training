from pydantic import BaseModel
from typing import List,Optional

class Developer(BaseModel):
    name: str
    experience: Optional[str]=None
class Project(BaseModel):
    title: str
    description: Optional[str]=None
    language: Optional[List[str]]=[]
    lead_developer: Developer

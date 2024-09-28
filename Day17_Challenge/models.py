from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Pydantic Models
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

class RecipeBase(BaseModel):
    name: str
    description: Optional[str] = None
    ingredients: str
    instructions: str
    cuisine: str
    difficulty: str
    category_id: Optional[int] = None

class RecipeCreate(RecipeBase):
    pass

class RecipeResponse(RecipeBase):
    id: int

# SQLAlchemy Models
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    recipes = relationship("Recipe", back_populates="category")

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    ingredients = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)
    cuisine = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True)

    category = relationship("Category", back_populates="recipes")

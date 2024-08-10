from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(..., alias="name")
    description: str = Field(..., alias="description")
    price: float = Field(..., alias="price")
    duration: float = Field(..., alias="duration")

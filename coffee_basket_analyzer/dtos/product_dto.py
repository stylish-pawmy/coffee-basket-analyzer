from pandas import DataFrame, Series
from pydantic import BaseModel

class ProductDto(BaseModel):
    id: int
    category: str
    type: str
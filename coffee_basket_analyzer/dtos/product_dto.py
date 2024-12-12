from pandas import DataFrame, Series
from pydantic import BaseModel

class ProductDto(BaseModel):
    def __init__(self, product_entry: Series):
        self.id = int(product_entry["product_id"])
        self.category = str(product_entry["product_category"])
        self.type = str(product_entry["product_type"])
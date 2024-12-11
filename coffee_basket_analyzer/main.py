import pandas as pd
from fastapi import FastAPI

from dtos.product_dto import ProductDto
from services.basket_service import BasketService

app = FastAPI()

sales = pd.read_excel("../data/raw/Coffee Shop Sales.xlsx")
sales.reset_index(inplace=True)

@app.get("/products/{id}")
async def GetProductById(id: int):
    return ProductDto(sales.iloc[id])


@app.get("/products")
async def GetAllProducts():
    products: pd.DataFrame = BasketService.get_distinct_products(sales)
    return [ ProductDto(row) for _, row in products.iterrows()]
import pandas as pd
from typing import List
from fastapi import FastAPI, Body

from dtos.product_dto import ProductDto
from dtos.rule_dto import RuleDto
from services.basket_service import BasketService
from services.fpgrowth_service import FpGrowthService

app = FastAPI()

sales = pd.read_excel("../data/raw/Coffee Shop Sales.xlsx")
sales.reset_index(inplace=True)
distinct_products: pd.DataFrame = BasketService.get_distinct_products(sales)

@app.get("/products/{id}")
async def GetProductById(id: int):
    return ProductDto(sales.iloc[id])


@app.get("/products")
async def GetAllProducts():
    products_response = []

    for _, row in distinct_products.iterrows():
        product = ProductDto(
            id = int(row["product_id"]),
            category = str(row["product_category"]),
            type = str(row["product_type"])
        )
        products_response.append(product)
        
    return {"products" : products_response}


@app.post("/rules")
async def FindRules(
    products: List[str] = Body(...),
    metric: str = Body(...),
    threshold: float = Body(...)
    ):

    itemsets = pd.read_pickle("../models/fpgrowth-model.pkl")
    filtered_rules = FpGrowthService.LoadRules(itemsets, products, metric, threshold)

    rules = []
    for _, row in filtered_rules.iterrows():
        rules.append(
            RuleDto(
                consequents=list(row["consequents"]),
                antecedents=list(row["antecedents"]),
                support=row["support"],
                confidence=row["confidence"],
                lift=row["lift"]
            )
        )
    
    return {"rules": rules}
from pandas import DataFrame, Series
import numpy as np

class BasketService:
    @staticmethod
    def same_basket(df: DataFrame, i: int, j: int, attr = list[str]) -> bool:
        if i == j: return False

        state = True
        for attribute in attr: 
            state = state and df.loc[i, attribute] == df.loc[j, attribute]
        return state

    
    @staticmethod
    def get_distinct_products(df):
        distinct_products = df.drop_duplicates(subset="product_type", inplace=False)
        return distinct_products[["product_id", "product_type", "product_category"]]


    @staticmethod
    def create_baskets(df: DataFrame,
                      item_descriptor: str="product_type",
                      date: str="transaction_date",
                      time: str="transaction_time",
                      store: str="store_id"):
        
        """
        Groups products bought together into baskets.

        Args:
            data (pd.DataFrame): Input dataframe with columns 'transaction_date', 'transaction_time', 'store_id', and 'product_type'.

        Returns:
            list of lists: Each sublist contains products bought together as part of the same basket.
        """
        # Create a unique basket identifier using date, time, and store_id
        df['basket_id'] = df[date].astype(str) + "_" + \
                            df[time].astype(str) + "_" + \
                            df[store].astype(str)

        # Group by the unique basket identifier and aggregate the product types into lists
        baskets = df.groupby('basket_id')[item_descriptor].apply(list).tolist()

        return baskets
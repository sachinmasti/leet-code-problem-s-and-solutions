import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby('customer_number')['customer_number'].count()
    result = orders.idxmax()

    return pd.DataFrame(columns=['customer_number'],data=[result])
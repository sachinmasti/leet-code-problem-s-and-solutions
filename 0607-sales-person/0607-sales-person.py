import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    df = orders.merge(company,how='left',on='com_id')

    filtered = df[df['name'] == 'RED']['sales_id']

    return sales_person[~sales_person['sales_id'].isin(filtered)] [['name']]
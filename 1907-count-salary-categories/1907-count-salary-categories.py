import pandas as pd
import numpy as np

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts['category'] = np.select(condlist=[accounts['income'] < 20000,
    accounts['income'].between(20000,50000),
    accounts['income'] > 50000],
    choicelist=['Low Salary','Average Salary','High Salary'],
    default='Not Valid')

    accounts['category'] = pd.Categorical(
        accounts['category'], 
        categories=['Low Salary', 'Average Salary', 'High Salary']
    )

    accounts = accounts.groupby(['category'], observed=False)['account_id'].count().reset_index()

    return accounts.rename(columns={'account_id':'accounts_count'})
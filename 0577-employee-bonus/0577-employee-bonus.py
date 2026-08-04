import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    new_df = employee.merge(bonus,how='outer',on='empId')
    return new_df[(new_df['bonus'] < 1000) | (new_df['bonus'].isna())] [['name','bonus']]
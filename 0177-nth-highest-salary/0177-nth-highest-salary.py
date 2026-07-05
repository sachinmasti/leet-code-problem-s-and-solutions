import pandas as pd
import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salary = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if N <= 0 or len(unique_salary) < N:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})

    nth_salary = unique_salary.iloc[N-1]

    return pd.DataFrame({f'getNthHighestSalary({N})':[nth_salary]})
    
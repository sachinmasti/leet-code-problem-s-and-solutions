import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee.drop_duplicates(subset='salary').sort_values(by='salary',ascending=False)
    if unique_salaries.shape[0] <=1:
        return pd.DataFrame(columns=['SecondHighestSalary'],data=[pd.NA])

    value = unique_salaries['salary'].iloc[1]
    new_df =  pd.DataFrame(columns=['SecondHighestSalary'],data=[value])
    return new_df
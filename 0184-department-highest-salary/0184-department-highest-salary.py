import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    result = employee.merge(department,how='inner',left_on='departmentId',right_on='id')

    filter_mask = result['salary'] == result.groupby('name_y')['salary'].transform('max')

    new = result[filter_mask]

    new = new.rename(columns={
    'name_y': 'Department', 
    'name_x': 'Employee', 
    'salary': 'Salary'})

    return new[['Department', 'Employee', 'Salary']]
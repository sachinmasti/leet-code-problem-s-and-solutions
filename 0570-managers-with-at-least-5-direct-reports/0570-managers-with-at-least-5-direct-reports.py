import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    id = employee['managerId'].value_counts()

    filterd = id[id >= 5].index
    
    return employee[employee['id'].isin(filterd)][['name']]
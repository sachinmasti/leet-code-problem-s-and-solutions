import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    result = my_numbers.drop_duplicates(keep=False).max()
    return  pd.DataFrame(columns=['num'],data=result.values)
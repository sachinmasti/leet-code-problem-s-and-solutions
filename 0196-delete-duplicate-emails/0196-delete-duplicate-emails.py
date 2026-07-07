import pandas as pd
import numpy as np

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    df = person.sort_values(by='id',inplace=True)
    df = person.drop_duplicates(subset='email',keep='first',inplace=True)
    
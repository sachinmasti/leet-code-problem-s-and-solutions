import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    filtered = courses.groupby('class').size().reset_index(name='count')
    result = filtered[filtered['count'] >= 5] [['class']]
    return result
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    result =  actor_director.groupby(['actor_id','director_id'],as_index=False).count()

    return result.query('timestamp >=3')[['actor_id','director_id']]
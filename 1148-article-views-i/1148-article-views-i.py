import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result = views[views['author_id'] == views['viewer_id']]['author_id'].unique()
    new_df =  pd.DataFrame(result,columns=['id'])
    return new_df.sort_values(by='id',ascending=True)
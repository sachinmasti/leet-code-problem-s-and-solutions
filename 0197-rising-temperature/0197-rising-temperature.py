import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    result =  weather.sort_values(by='recordDate',ascending=True)
    result['prev_temp'] = result['temperature'].shift(1)
    result['prev_date'] = result['recordDate'].shift(1)
    return result[(result['temperature'] > result['prev_temp']) & (result['recordDate'] - result['prev_date'] == pd.Timedelta(days=1))] [['id']]
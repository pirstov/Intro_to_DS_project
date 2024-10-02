import requests
import pandas as pd

WEATHER_API_ENDPOINT = 'https://api.open-meteo.com/v1/forecast'


def get_weather_forecast(latitude:float=60.192059,
                        longitude:float=24.945831,
                        forecast_days:int=7,
                        past_days:int=0) -> pd.DataFrame|None:
    """Get weather forecast data from open-meteo api

    Args:
        latitude (float, optional): Latitude of location. Defaults to 60.192059 latitude of helsinki finland.
        longitude (float, optional): Longitude of location. Defaults to 24.945831 longitude of helsinki finland.
        forecast_days (int, optional): Number of days to forecast. Defaults to 7. Accepted Range 0-16
        past_days (int, optional): Number of past days to include in data. Defaults to 0. Accepted Range 0-92

    Returns:
        pd.DataFrame|None: dataframe containing weather forecast on success. dataframe has columns : time, temperature, wind_speed. Returns None on failure.
        
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "forecast_days": forecast_days,
        "past_days": past_days,
        "temperature_unit": 'celsius',
        "wind_speed_unit": 'ms',
        "hourly": ['temperature_2m','wind_speed_10m']
    }

    try:
        response = requests.get(WEATHER_API_ENDPOINT, params=params)

        if response.status_code == 200:
            data = response.json()

            forecast = pd.DataFrame(data['hourly']).rename(columns={'temperature_2m':'temperature','wind_speed_10m':'wind_speed'})
            return forecast
        else:
            print(f'Error getting data. Response code: {response.status_code}')
            return None
        
    except Exception as e:
        print("An exception occurred:", e)
        return None



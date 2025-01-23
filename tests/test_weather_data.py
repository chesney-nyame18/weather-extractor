import sys, os, datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.fetch_weather_data import FetchRawWeatherData
# from lambda_function import lambda_handler

import pytest

def test_missing_keys():
    # -- sample weather data
    current_weather = {'coord': {'lon': -2.1364, 'lat': 57.1269}, 'weather': [{'id': 801}], 'base': 'stations', 'main': {'feels_like': 281.5, 'pressure': 1037, 'humidity': 75}, 'visibility': 10000, 'wind': {'speed': 2.06, 'deg': 170}, 'clouds': {'all': 19}, 'dt': 1642429743, 'sys': {'type': 2, 'id': 2031790, 'country': 'GB', 'sunrise': 1642408438, 'sunset': 1642435368}, 'timezone': 0, 'id': 2657832, 'name': 'Aberdeen', 'cod': 200}
    
    extractor = FetchRawWeatherData
    
    expected_output_weather_main = 'Not Provided'
    expected_output_weather_description = 'Not Provided'
    expected_output_weather_icon = 'Not Provided'

    
    weather_main = FetchRawWeatherData._fetch_values(current_weather['weather'][0], 'main', 'Not Provided')
    weather_description = FetchRawWeatherData._fetch_values(current_weather['weather'][0], 'description', 'Not Provided')
    weather_icon = FetchRawWeatherData._fetch_values(current_weather['weather'][0], 'icon', 'Not Provided')    

    actual_output_weather_main = weather_main
    actual_output_weather_description = weather_description
    actual_output_weather_icon = weather_icon

    assert expected_output_weather_main == actual_output_weather_main
    assert expected_output_weather_description == actual_output_weather_description
    assert expected_output_weather_icon == actual_output_weather_icon


# def test_none_type_values():
#     current_weathers = {'coord': {'lon': -1.1682, 'lat': 60.1517}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': None, 'feels_like': 276.89, 'temp_min': None, 'temp_max': None, 'pressure': 1029, 'humidity': 80, 'sea_level': 1029, 'grnd_level': 1028}, 'visibility': 10000, 'wind': {'speed': 9, 'deg': 271, 'gust': 12.26}, 'clouds': {'all': 100}, 'dt': 1642437669, 'sys': {'type': 1, 'id': 1438, 'country': 'GB', 'sunrise': 1642409427, 'sunset': 1642433914}, 'timezone': 0, 'id': 2644605, 'name': 'Lerwick', 'cod': 200}  
    
#     extractor = FetchRawWeatherData
    
#     area_temp = FetchRawWeatherData._fetch_values(current_weathers['main'], 'temp', 'Not Provided')

    
#     cleaned_area_temp = FetchRawWeatherData._convert_temp_to_none(area_temp)
    
#     expected_output_area_temp = None
    
#     actual_output_area_temp = cleaned_area_temp

#     assert expected_output_area_temp == actual_output_area_temp


# def test_average_temp_to_none():
#     current_weathers  = {'coord': {'lon': -1.1682, 'lat': 60.1517}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 'string', 'feels_like': 276.89, 'temp_min': 'string', 'temp_max': 'string', 'pressure': 1029, 'humidity': 80, 'sea_level': 1029, 'grnd_level': 1028}, 'visibility': 10000, 'wind': {'speed': 9, 'deg': 271, 'gust': 12.26}, 'clouds': {'all': 100}, 'dt': 1642437669, 'sys': {'type': 1, 'id': 1438, 'country': 'GB', 'sunrise': 1642409427, 'sunset': 1642433914}, 'timezone': 0, 'id': 2644605, 'name': 'Lerwick', 'cod': 200}  
    
#     extractor = FetchRawWeatherData

#     area_temp = extractor._fetch_values(current_weathers['main'], 'temp', 'Not Provided')

#     cleaned_area_temp, cleaned_area_min_temp, cleaned_area_max_temp = extractor._convert_temp_to_none(area_temp)
    
#     cleaned_average_temp = extractor._create_avg_temp(cleaned_area_temp, cleaned_area_min_temp, cleaned_area_max_temp) 
    
#     actual_output_average_temp = cleaned_average_temp
    
#     expected_output_average_temp = None
    

    
#     assert expected_output_average_temp == actual_output_average_temp



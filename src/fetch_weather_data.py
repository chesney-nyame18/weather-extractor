import logging
from requests import get
from json import loads
from time import sleep
from datetime import datetime

from src.geographic_coordinates import geo_coordinates

log = logging.getLogger("__main__")


class FetchRawWeatherData:

    @staticmethod
    def _request(latitude, longitude):
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=2e54ec1eac671aa0d40c3bfde21aab42"
            request = get(url)
            return request
        except Exception as ex:
            log.error(f"api request failed: {ex}")
    
    @staticmethod
    def _process_request(request):
        try:
            if request.status_code == 200:
                response = loads(request.content.decode('utf-8'))
                return response
            else:
                log.exception(f"request failed with status {request.status_code}")
            
        except Exception as error:
            log.exception(error)
    
    @staticmethod
    def _fetch_values(weather_details, key, default):
        if key in weather_details:
            return weather_details[key]
        else:
            return default
    
    @staticmethod
    def _clean_values(weather_details):
        cleansed_data = {}
        try:
            main = FetchRawWeatherData._fetch_values(weather_details['weather'][0], 'main', 'Not Provided')
            description = FetchRawWeatherData._fetch_values(weather_details['weather'][0], 'description', 'Not Provided')
            icon = FetchRawWeatherData._fetch_values(weather_details['weather'][0], 'icon', 'Not Provided')
            temperature = FetchRawWeatherData._fetch_values(weather_details['main'], 'temp', 'Not Provided')
            feel_like_temperature = FetchRawWeatherData._fetch_values(weather_details['main'], 'feels_like', 'Not Provided')
            max_temperature = FetchRawWeatherData._fetch_values(weather_details['main'], 'temp_max', 'Not Provided')
            min_temperature = FetchRawWeatherData._fetch_values(weather_details['main'], 'temp_min', 'Not Provided')
            air_pressure = FetchRawWeatherData._fetch_values(weather_details['main'], 'pressure', 'Not Provided')
            humidity = FetchRawWeatherData._fetch_values(weather_details['main'], 'humidity', 'Not Provided')
            wind_speed = FetchRawWeatherData._fetch_values(weather_details['wind'], 'speed', -1)
            wind_degree = FetchRawWeatherData._fetch_values(weather_details['wind'], 'deg', -1)
            sunrise = FetchRawWeatherData._fetch_values(weather_details['sys'], 'sunrise', 'Not Provided')
            sunset = FetchRawWeatherData._fetch_values(weather_details['sys'], 'sunset', 'Not Provided')
            city = FetchRawWeatherData._fetch_values(weather_details, 'name', 'Not Provided')
            
            cleansed_data['main'] = main
            cleansed_data['description'] = description
            cleansed_data['icon'] = icon
            cleansed_data['temperature'] = temperature
            cleansed_data['feels_like'] = feel_like_temperature
            cleansed_data['max_temperature'] = max_temperature
            cleansed_data['min_temperature'] = min_temperature
            cleansed_data['air_pressure'] = air_pressure
            cleansed_data['humidity'] = humidity
            cleansed_data['wind_speed'] = wind_speed
            cleansed_data['wind_degree'] = wind_degree
            cleansed_data['sunrise'] = sunrise
            cleansed_data['sunset'] = sunset
            cleansed_data['city'] = city
            
            return cleansed_data
        except:
            log.error()
        return
    
    def collect_weather_data(self):
        dataset = []
        for postcode in geo_coordinates:
            latitude = geo_coordinates[postcode][0]
            longitude = geo_coordinates[postcode][1]
            
            request = FetchRawWeatherData._request(latitude, longitude)
            response = FetchRawWeatherData._process_request(request)
            
            log.debug(f"fetching weather details for {postcode} at {datetime.now()} ")
            data = FetchRawWeatherData._clean_values(response)
            dataset.append(data)
            
            sleep(1)
        return dataset
'''imports
'''
import os
import logging
from logging_setup import log_init
from datetime import datetime

if __name__ in ("__main__", "lambda_function"):
    from src.fetch_weather_data import FetchWeatherData  # Update module file here
else:
    from .src.fetch_weather_data import FetchWeatherData  # Update module file here

# Configure Logging
log = logging.getLogger("__main__")

if __name__ == "lambda_function":
    log_init(log, debug=True, plain_text_log=False)
else:
    log_init(log, debug=True, plain_text_log=True)


def lambda_handler(event, context):
    '''Runs fetch_weather_data.py
    '''
    start_time = datetime.now()
    log.info(f"Lambda Started: {start_time}")
    log.info(f"Starting weather data collection: {start_time}")

    fetch_weather_data = FetchWeatherData()
    output_raw_dataset = fetch_weather_data.collect_weather_data()
    
    end_time = datetime.now()
    log.info(f"Completed weather data collection {end_time}")
    log.info("Lambda finished")


if __name__ == "__main__":
    lambda_handler(None, None)


'''imports
'''
import os
import logging
from logging_setup import log_init
from datetime import datetime
from aws_sdk import aws_get_s3_client
import json

if __name__ in ("__main__", "lambda_function"):
    from src.fetch_weather_data import FetchRawWeatherData  # Update module file here
else:
    from .src.fetch_weather_data import FetchRawWeatherData  # Update module file here

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

    output_raw_dataset = FetchRawWeatherData().collect_weather_data()
    
    #write raw data to s3
    aws_profile = os.getenv('AWS_PROFILE')
    s3_client = aws_get_s3_client(aws_profile)
    bucket_name = 'dev-ingestion-labs'
    year = start_time.strftime('%Y')
    month = start_time.strftime('%m')
    day = start_time.strftime('%d')
    hour = start_time.strftime('%H')
    file_name = f"weather_data_{hour}00.json"
    s3_key = f"weather_data/year={year}/month={month}/day={day}/hour={hour}/{file_name}"
    file_name = f"weather_data_{start_time.strftime('%Y%m%d%H%M%S')}.json"
    s3_client.put_object(
        Bucket=bucket_name,
        Key=s3_key,
        Body=json.dumps(output_raw_dataset)
    )
    
    end_time = datetime.now()
    log.info(f"Completed weather data collection {end_time}")
    log.info("Lambda finished")


if __name__ == "__main__":
    lambda_handler(None, None)


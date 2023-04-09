import os
import logging
import pandas as pd
import re
import json
import datetime as dt
from pyspark.sql.functions import pandas_udf
logging.basicConfig(level=logging.INFO,filename="log.txt")
from googletrans import Translator
import requests
from bs4 import BeautifulSoup
import psycopg2

validation_para={
    'banner':"DE",
    "json_location":"/home/aryan/Music/YouTube_Analysis_Data/DE_category_id.json",
    "csv_location":"/home/aryan/Music/YouTube_Analysis_Data/DEvideos.csv",
    "table_name":"dedata",
    "validated_file_location":"/home/aryan/data_pipeline/"
}
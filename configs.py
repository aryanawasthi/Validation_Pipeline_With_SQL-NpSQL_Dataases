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

formatter = logging.Formatter('%(message)s')
logging.basicConfig(level=logging.INFO,Formatter=formatter,filename='log.txt')





#
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass

sys.path.append(os.path.join(os.getcwd(), "src"))
from datascience.logger import logging
from datascience.exception_handling import CustomException
from dotenv import load_dotenv
import pymysql


load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from studentsperformance',mydb)
        print(df.head())

        return df

    except Exception as ex:
        raise CustomException(ex)
    

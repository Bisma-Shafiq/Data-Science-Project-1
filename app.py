import sys
import os
sys.path.append(os.path.join(os.getcwd(), "src"))
from datascience.logger import logging
from datascience.exception_handling import CustomException
from datascience.components.data_ingestion import DataIngestion
from datascience.components.data_ingestion import DataIngestionConfig


if __name__=='__main__':
    logging.info("Execution")

    try:
         #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()

    except Exception as e:
            logging.info("Excetional_handling")
            raise CustomException(e,sys)




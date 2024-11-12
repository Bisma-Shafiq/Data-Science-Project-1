import sys
import os
sys.path.append(os.path.join(os.getcwd(), "src"))

from datascience.logger import logging
from datascience.exception_handling import CustomException

if __name__=='__main__':
    logging.info("Execution")

    try:
        a=1/0
    except Exception as e:
        logging.info("Excetional_handling")
        raise CustomException(e,sys)




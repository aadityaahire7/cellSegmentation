from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
import sys

logging.info("Welcome To the Custom Log")

try:
    a=4/"6"

except Exception as e:
    raise AppException(e,sys)

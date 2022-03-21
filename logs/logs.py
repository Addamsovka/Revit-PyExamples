# Made by Addamsovka
# Log Python script errors to .txt
import logging

file_path = IN[0] # input file path

# Set logger
logger = logging.getLogger(__name__)  
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(file_path)
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

try:
	# Logs
	logger.debug('------------------------------------')
	logger.debug('Start testing.')
	# Write code for testing here
	logger.info('Code passed.')
except Exception as inst:
    logger.error(inst)
    
OUT = "Done"

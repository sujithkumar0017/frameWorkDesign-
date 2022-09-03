"""import logging

class Logged:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='auto.log',format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.debug("this is debug mode")
        logger.info("this is debug mode")
        logger.error("this is debug mode") """


#importing the module
import logging

'''class LogGen:
    @staticmethod
    def loggen():
        #now we will Create and configure logger
        logging.basicConfig(filename="std.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            filemode='w')
        #Let us Create an object
        logger=logging.getLogger()
        #Now we are going to Set the threshold of logger to DEBUG
        logger.setLevel(logging.INFO)
        return logger '''

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.//Logs//automation.log',mode='a')
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger

#1. Create Logger
#2. Create console handler or file handler and set the log level
#3. Create Formatter - how you want your logs to be formatted.
#4. add formatter to console or file handler
  # To print in Console:
    #ch = logging.StreamHandler()
    #ch.SetFormatter(formatter)
#5. Application Code - log message.
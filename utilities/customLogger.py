import logging

class LogGen:
    @staticmethod
    def loggen():
         logging.basicConfig(filename="C://Users//USER//PycharmProjects//nopcommerceapp//Logs\\automation.log",
                        format='%(asctime)s %(levelname)s %(message)s:',datefmt='%Y/%M/%D %H:%M:%S %P')
         logger=logging.getLogger()
         logger.setLevel(logging.INFO)
         return logger
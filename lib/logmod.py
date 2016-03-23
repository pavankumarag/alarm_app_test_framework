import logging
import datetime

def configure_log(level=None, name=None, filename=None):
    """
    This function configures the logger module(uses standdard logging module of python) setting level to DEBUG
    and setting timestamp to %Y:%m:%dT%H:%M:%S format. This will return logger object.  
    """
    logger = logging.getLogger(__name__) 
    logger.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    chFormatter = logging.Formatter("%(asctime)s      %(levelname)s      %(message)s",
                              "%Y:%m:%dT%H:%M:%S")
    console_handler.setFormatter(chFormatter)
    logger.addHandler(console_handler)
    
    hdlr = logging.FileHandler(filename,"w")
    hdlr.setFormatter(chFormatter)
    logger.addHandler(hdlr)
    
    return logger


import logging
import time
import MudConst
import sys
import traceback

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=MudConst.log_dir+str(time.strftime("%a %d %b %Y", time.gmtime()))+'.txt',
                    filemode='w')


def logTraceback():
    """
    A function to write a traceback to the log.
    For now, we'll also print the exception to
    the screen as well.
    """
    logging.error("Error in execution: " + str(sys.exc_info()[0]) + "\r\n" + listf(format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)))
    print "Error in execution: " + str(sys.exc_info()[0]) + "\r\n" + listf(format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback))


def listf(data):
    """
    This function will format the output of a traceback.
    I'm putting it here, because it seems fitting and I
    don't want to have to redefine the behavior everywhere
    we want to use tracebacks to find out what's going on.
    """
    buffer = ""
    for line in data:
        buffer = buffer + line + "\n"
    return buffer

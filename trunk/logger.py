import logging
import time
import MudConst

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=MudConst.log_dir+str(time.time())+'.txt',
                    filemode='w')

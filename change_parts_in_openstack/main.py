# -*- coding: utf-8 -*-

import os 
from constants import *
from pool import Pool
import time
import logging


def main():
    logger = logging.getLogger('main')
    logger.setLevel(logging.INFO)
    # create file handler
    fh = logging.FileHandler('main.log')
    fh.setLevel(logging.INFO)
    # create console handler 
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # set formatter

    formatter = logging. \
        Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    start = time.time()
    logger.info('start time is : %s' % str(start))
    logger.info('initiate pool')
    pool = Pool()
    pool.start_task()
    pool.wait_all_complete()

    # print info
    logger.info("花费时间： %s秒" %str(time.time() - start))

if __name__ == "__main__":
    main()
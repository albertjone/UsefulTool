# -*- coding: utf-8 -*-

import os 
from constants import *
from pool import Pool
import time



            


def main():
    start = time.time()
    pool = Pool()
    pool.start_task()
    pool.wait_all_complete()

    #print info
    print("花费时间： {0} 秒".format(time.time()-start))

if __name__ == "__main__":
    main()
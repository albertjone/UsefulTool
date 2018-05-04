import os 
import logging
import greenlet
import traceback
from eventlet.queue import Queue
from constants import *
from commiter import Commiter
from collector import Collector


def spawn(*args,**kwargs):
    def _launch(func,*args,**kwargs):
        try:
            func(*args,**Kwargs)
        except greenlet.GreenletExit:
            pass
        except:
            pass
    return greenlet.spawn(_launch,*args,**kwargs)

def collector(queue,notify):
    try:
        pass

            


def main():
    pass
if __name__ == "__main__":
    main()
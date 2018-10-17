#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from oslo_log import log as logging
from oslo_config import cfg

LOG = logging.getLogger(__name__)
CONF = cfg.CONF
DOMAIN = 'util'

logging.register_options(CONF)
logging.set_defaults(CONF, DOMAIN)
extra_log_level_defaults = [
    'main=INFO',
    'main=ERROR',
    'util=INFO',
    'util=ERROR'
]
logging.set_defaults(default_log_levels=extra_log_level_defaults)


# dir must be absoutly url
def get_file_by_name(dir, file_name):
    print()
    dirs = os.listdir(dir)
    for item in dirs:
        if(os.path.isdir(item)):
            dir = dir + item + '/'
            get_file_by_name(dir, file_name)           
        else:
            if(item == file_name):
                file_path = dir + item
                LOG.info('get file:' + dir)
                return file_path

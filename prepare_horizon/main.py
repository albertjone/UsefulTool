#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import platform
from oslo_log import log as logging
from oslo_config import cfg
import util

LOG = logging.getLogger(__name__)
CONF = cfg.CONF
DOMAIN = 'main'

logging.register_options(CONF)
logging.setup(CONF, DOMAIN)

extra_log_level_defaults = [
    'main=INFO',
    'main=ERROR',
    'util=INFO',
    'util=ERROR'
]
logging.set_defaults(default_log_levels=extra_log_level_defaults)


mac_list = ['Darwin']
debian_list = []
centos_list = []


def get_known_hosts():
    sys = platform.system()
    if sys in mac_list:
        LOG.info('the system is mac')
        home_dir = os.path.expanduser('~') + '/'
        LOG.info('the current dir:' + home_dir)
        known_hostspath = util.get_file_by_name(home_dir, 'known_hosts')
        print(known_hostspath)
        if not known_hostspath:
            return "error"
    if sys in debian_list:
        LOG.info('the system is not linux')
    return None


def main():
    # delete known_hosts
    known_hosts = get_known_hosts()
    if not known_hosts:
        LOG.error("there exists no known_hosts")


if __name__ == "__main__":
    main()

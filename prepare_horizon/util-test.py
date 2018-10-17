#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util

dir = "/Users/robot/.ssh"
file_name = "known_hosts"
file_path = util.get_file_by_name(dir, file_name)
print file_path
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/25 17:37 
# @Author : huangke
# @Email : huangke10@foxmail.com

import sys
import os
root_path = os.path.abspath(__file__)
root_path = os.path.split(root_path)[0]
root_path = os.path.split(root_path)[0]
sys.path.append(root_path)

from shuttle import logger

def test_logging_context():
    with logger(filename='log.txt', mode='a', stdout=True) as log:
        print('log context sucessed')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/25 17:30 
# @Author : huangke
# @Email : huangke10@foxmail.com

import sys
import os
root_path = os.path.abspath(__file__)
root_path = os.path.split(root_path)[0]
root_path = os.path.split(root_path)[0]
sys.path.append(root_path)

from .draw_interface import draw_func
from .table_interface import table_func
from shuttle import shuttle
from shuttle import logger
from shuttle import import_all_eval_modules_for_shuttle


@logger(filename='log.txt', mode='a', stdout=True)
def main():
    import_all_eval_modules_for_shuttle()
    draw_ret = draw_func('draw_value')
    table_ret = table_func('table_value')
    shuttle.check()
    draw_ret = draw_func('value')
    table_ret = table_func('value')
    shuttle.check()


def test_basic_usage():
    main()
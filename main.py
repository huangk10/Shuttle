#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/22 17:30 
# @Author : huangke
# @Email : huangke10@foxmail.com

from draw_interface import draw_func
from table_interface import table_func
from shuttle import shuttle
from shuttle import import_all_eval_modules_for_shuttle



def main():
    import_all_eval_modules_for_shuttle()
    draw_ret = draw_func('draw_value')
    table_ret = table_func('table_value')
    shuttle.check()
    draw_ret = draw_func('value')
    table_ret = table_func('value')
    shuttle.check()
    print(shuttle.vals)


if __name__ == '__main__':
    main()
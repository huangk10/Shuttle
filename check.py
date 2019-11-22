#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/22 17:28 
# @Author : huangke
# @Email : huangke10@foxmail.com


from shuttle import shuttle


@shuttle.evaluate
def eval_draw_and_table(dict_file):
    if dict_file['draw_func']['画图接口指标'] == dict_file['table_func']['表格接口指标']:
        print('接口指标一致')
    else:
        print('接口指标不一致')
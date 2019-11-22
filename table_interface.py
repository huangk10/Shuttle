#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/22 17:25 
# @Author : huangke
# @Email : huangke10@foxmail.com


from shuttle import shuttle


@shuttle.register({'表格接口指标': 'table_arg'})
def table_func(table_arg):
    table_arg = table_arg
    table_func.locals = locals()
    return table_arg
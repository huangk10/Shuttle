#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/22 17:24 
# @Author : huangke
# @Email : huangke10@foxmail.com


from shuttle import shuttle


@shuttle.register({'画图接口指标': 'draw_arg'})
def draw_func(draw_arg):
    draw_arg = draw_arg
    draw_func.locals = locals()
    return draw_arg
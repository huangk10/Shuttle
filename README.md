# Shuttle
![Travis (.org) branch](https://img.shields.io/travis/huangk10/Shuttle/master)

用于数据分析报告图表接口间指标一致性校验的工具，包括指标收集、检测接口、指标序列化、指标批量对比和日志等功能。

## 具体用法

### 指标收集

指标收集是通过`shuttle.register`作为装饰器实现，需要对原始接口进行侵入性改造。

`register`参数内容为`dict`, 其中`key`为指标定义的标准名称, `value`为指标在接口内部的变量名称。

```python
from shuttle import register

@register({"画图接口指标": 'draw_arg'})
def draw_interface_function(draw_arg):
    """画图接口函数"""
    draw_arg = draw_arg
    # ! 侵入性改造
    draw_interface_function.locals = locals()
    return 
```

### 检测接口

需要为所有检测接口添加`shuttle.evaluate`装饰器，且所有检测接口只有一个`dict_file`字典类型参数。获取指标的方式为`dict_file[函数名称][定义指标标准名称]`

```python
from shuttle import evaluate

@evaluate
def eval_draw_and_table(dict_file):
    if dict_file['draw_func']['画图接口指标'] == dict_file['table_func']['表格接口指标']:
        print('表格和画图指标一致')
    else:
        print('表格和画图指标不一致')
```

### 指标序列化

指标序列化的目的是将收集的指标储存到本地，用于后续对比分析。

```python
from shuttle import shuttle

"""after some interfaces called"""
shuttle.serialize("place where you want to save")
```

### 指标批量对比

指标批量对比可以对接口的修改进行检测

```python
from shuttle import shuttle

old_dict = shuttle.deserialize("old file place you saved")
new_dict = shuttle.deserialize("new file place you saved")
shuttle.compare_dicts(new_dict, old_dict)
```

### 日志模块

日志模块的作用是快速形成日志文件，只需要为调用函数增加一个`logger`装饰器，即可以将函数内部中`print`中内容输出到日志文件，适合快速开发。

```python
from shuttle import logger

@logger(filename='log.txt', mode='a', stdout=False)
def my_func():
    print('some logs needs to be logged in file')

    
my_func()
```

### 检测接口批量调用

```python
from shuttle import shuttle
from shuttle import logger
from shuttle import import_all_eval_modules_for_shuttle
from draw_interface import draw_func
from table_interface import table_func

@logger(filename='log.txt', mode='a', stdout=True)
def main():
    import_all_eval_modules_for_shuttle()
    draw_func()
    table_func()
    shuttle.check() # 指标检测并输出日志

main()
```


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
import pickle


class Logger:
    _sys = __import__('sys')

    def __init__(self, filename, mode):
        self.terminal = self._sys.__stdout__
        self.log = open(filename, mode)

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def close(self):
        self.log.close()


class Shuttle:

    _sys = __import__('sys')
    _functools = __import__('functools')
    _Logger = Logger

    def __init__(self):
        self.ref = {}
        self.vals = {}
        self.evals = {}

    def register(self, arg_dict):
        def decorator(func):
            def inner(*args, **kwargs):
                result = func(*args, **kwargs)
                # when call the function firstly
                if func.__name__ not in self.ref:
                    self.ref.update({func.__name__: 0})
                    self.vals.update({func.__name__: {}})
                    for key, value in arg_dict.items():
                        self.vals[func.__name__].update({key: inner.__dict__['locals'][value]})
                else:
                    self.ref[func.__name__] += 1
                    new_func_name = f"{func.__name__}-{self.ref[func.__name__]}"
                    self.vals.update({new_func_name: {}})
                    for key, value in arg_dict.items():
                        self.vals[new_func_name].update({key: inner.__dict__['locals'][value]})
                return result
            return inner
        return decorator

    def check(self):
        for func in self.evals.values():
            func(self.vals)

    def evaluate(self, func):

        def add(key, value):
            self.evals[key] = value
            return value

        if callable(func):
            return add(func.__name__, func)

        return lambda x: add(func, x)

    def serialize(self, file_path):
        with open(file_path, 'wb') as handler:
            pickle.dump(self.vals, handler, protocol=pickle.HIGHEST_PROTOCOL)

    def deserialize(self, file_path):
        with open(file_path, 'rb') as handler:
            ret_dict = pickle.load(handler)
        return ret_dict

    @staticmethod
    def compare_dicts(src_dict, tgt_dict, path=None):
        if path is None:
            path = ''
        # 递归
        if isinstance(src_dict, dict):
            for key in tgt_dict:
                if key in src_dict:
                    Shuttle.compare_dicts(src_dict[key], tgt_dict[key], path=path+f'["{key}"]')
                else:
                    path = path+f'["{key}"]'
                    print(f"src_dict路径{path}不存在")
        else:
            if str(src_dict) != str(tgt_dict):
                print(f"src_dict路径{path}值{src_dict}和tgt_dict路径{path}值{tgt_dict}不相等")

    def logger(self, filename, mode, stdout=True):
        def decorate(func):
            @self._functools.wraps(func)
            def warpper(*args, **kwargs):
                self._sys.stdout = self._Logger(filename, mode) if stdout else open(filename, mode)
                result = func(*args, **kwargs)
                self._sys.stdout.close()
                self._sys.stdout = self._sys.__stdout__
                return result
            return warpper
        return decorate



shuttle = Shuttle()
logger = shuttle.logger


EVAL_MODULE = [('', ['check'])]


def import_all_eval_modules_for_shuttle():
    for base_dir, modules in EVAL_MODULE:
        for name in modules:
            try:
                if base_dir != '':
                    full_name = base_dir + '.' + name
                else:
                    full_name = name
                importlib.import_module(full_name)
            except ImportError as error:
                print(f"Import error: {error}")

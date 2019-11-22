#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib



class Shuttle:

    def __init__(self):
        self.vals = {}
        self.evals = {}

    def register(self, arg_dict):
        def decorator(func):
            def inner(*args, **kwargs):
                result = func(*args, **kwargs)
                self.vals.update({func.__name__: {}})
                for key, value in arg_dict.items():
                    self.vals[func.__name__].update({key: inner.__dict__['locals'][value]})
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

    def jsonify(self, file_path):
        pass


shuttle = Shuttle()


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

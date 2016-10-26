# -*- coding: utf-8 -*-
import logging
from functools import wraps

__all__ = ['loggable_class', 'loggable_method']


def loggable_method(name):
    """
    Wraps a method to set logger on self.logger
    """
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kw):
            try:
                _self = args[0]
                _self.logger = logging.getLogger(name if isinstance(name, str) else _self.__module__)
            except Exception as e:
                pass
            result = func(*args, **kw)
            return result
        return wrapper
    if hasattr(name, '__call__'):
        return dec(name)
    return dec


def loggable_class(Cls):
    import inspect, types
    for name, fn in inspect.getmembers(Cls):
        if isinstance(fn, types.BuiltinMethodType):
            setattr(Cls, name, loggable_method(fn))
    return Cls

# -*- coding: utf-8 -*-
import logging
from functools import wraps
import inspect

__all__ = ['loggable_class', 'loggable_method', 'loggable']


def loggable(param):
    if inspect.isclass(param):
        return loggable_class(param)
    else:
        return loggable_method(param)

def loggable_method(name):
    """
    Wraps a method to set logger on self.logger
    """

    def dec(func):
        @wraps(func)
        def wrapper(*args, **kw):
            try:
                _self = args[0]
                _self.logger = logging.getLogger(
                    name if isinstance(name, str) else _self.__module__
                )
            except Exception:
                pass
            result = func(*args, **kw)
            return result

        return wrapper

    if hasattr(name, "__call__"):
        return dec(name)
    return dec


def loggable_class(Cls):
    Cls.logger = property(lambda self: logging.getLogger(self.__module__))
    return Cls

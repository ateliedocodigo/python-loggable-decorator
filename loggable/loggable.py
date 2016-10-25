# -*- coding: utf-8 -*-
import logging
from functools import wraps

__all__ = ['loggable_method']

def loggable_method(name):
    """
    Wraps a method to set logger on self.logger
    """
    def dec(func):
        @wraps(func)
        def wrapper(self, *args, **kw):
            try:
                self.logger = logging.getLogger(name)
            except Exception as e:
                pass
            result = func(self, *args, **kw)
            return result
        return wrapper
    if hasattr(name, '__call__'):
        return dec(name)
    return dec
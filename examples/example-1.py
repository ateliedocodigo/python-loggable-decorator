# -*- coding: utf-8 -*-
import logging
import sys

# this is just an example config
logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG
)

from loggable import loggable_method as loggable

class Example1(object):
    @loggable(__name__)
    def decorated_method_with_name(self):
        self.logger.debug("Debug decorated_method_with_name")
        print("This is a decorated method")

    @loggable
    def decorated_method_without_name(self):
        self.logger.debug("Debug decorated_method_without_name")
        print("This is a decorated method")

    def undecorated_method(self):
        print("This is an undecorated method")
        try:
            self.logger.debug("This trows an error")
        except Exception as e:
            print("Expected error: {}".format(e))


if __name__ == "__main__":
    Example1().decorated_method_with_name()
    Example1().decorated_method_without_name()
    Example1().undecorated_method()

# -*- coding: utf-8 -*-
from loggable import loggable


class Example1(object):
    @loggable
    def decorated_method_with_name(self):
        self.logger.debug("Debug decorated_method_with_name")
        print("This is a decorated method")


@loggable
class Example2(object):
    def decorated_method_one(self):
        self.logger.debug("Debug decorated_method_with_name")
        print("This is a decorated method")

    def decorated_method_two(self):
        self.logger.debug("Debug decorated_method_two")
        print("This is a decorated method")


if __name__ == "__main__":
    Example1().decorated_method_with_name()
    Example2().decorated_method_one()
    Example2().decorated_method_two()

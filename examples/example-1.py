# -*- coding: utf-8 -*-

from loggable import loggable_method as loggable

class Example1(object):
    @loggable(__name__)
    def decoratedmethod(self):
        self.logger.debug("Debug this")
        print("This is a decorated method")

    def undecoratedmethod(self):
        print("This is an undecorated method")
        try:
            self.logger.debug("This trows an error")
        except Exception as e:
            print("Expected error: {}".format(e))


if __name__ == "__main__":
    Example1().decoratedmethod()
    Example1().undecoratedmethod()
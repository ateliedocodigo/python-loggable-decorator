# -*- coding: utf-8 -*-

from loggable import loggable

class Example1(object):
    @loggable(__name__)
    def decoratedmethod(self):
        self.logger.debug("Debug this")

    def undecoratedmethod(self):
        try:
            self.logger.debug("This trows an error")
        except Exception as e:
            print(e)
import sys
from unittest import TestCase

from loggable import loggable_class, loggable_method, loggable


@loggable_class
class LoggableClassTestCase(TestCase):

    def test_loggable(self):
        with self.assertLogs(__name__, level="DEBUG") as ctx:
            self.logger.debug("Debug Test for class")
            self.assertEqual(ctx.output,['DEBUG:test.test_loggable:Debug Test for class'])

class LoggableMethodTestCase(TestCase):

    @loggable_method(__name__)
    def test_loggable_method(self):
        with self.assertLogs(__name__, level="DEBUG") as logs:
            self.logger.debug("Debug Test for method")
            self.assertEqual(logs.output, ['DEBUG:test.test_loggable:Debug Test for method'])

@loggable
class LoggableClassTestCase2(TestCase):

    def test_loggable2(self):
        with self.assertLogs(__name__, level="DEBUG") as ctx:
            self.logger.debug("Debug Test for class")
            self.assertEqual(ctx.output,['DEBUG:test.test_loggable:Debug Test for class'])

class LoggableMethodTestCase(TestCase):

    @loggable(__name__)
    def test_loggable_method2(self):
        with self.assertLogs(__name__, level="DEBUG") as logs:
            self.logger.debug("Debug Test for method")
            self.assertEqual(logs.output, ['DEBUG:test.test_loggable:Debug Test for method'])

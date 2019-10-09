# Python Loggable Decorator

[![PyPI version](https://badge.fury.io/py/loggable-decorator.svg)](https://badge.fury.io/py/loggable-decorator)


Add a logger attribute to class decorated

Installation
------------

```
pip install loggable-decorator
```

USAGE
-----

Decorate methods that you want to get logger like [example](examples/example-1.py)

```python
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
```

This will reproduce

```
$ python example-1.py
DEBUG:__main__:Debug decorated_method_with_name
This is a decorated method
DEBUG:__main__:Debug decorated_method_without_name
This is a decorated method
This is an undecorated method
Expected error: 'Example1' object has no attribute 'logger'
```


Decorate all methods in a class like [example](examples/example-2.py)


```python
# -*- coding: utf-8 -*-
import logging
import sys

# this is just an example config
logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG
)

from loggable import loggable_class as loggable

@loggable
class Example2(object):
    def decorated_method_one(self):
        self.logger.debug("Debug decorated_method_with_name")
        print("This is a decorated method")

    def decorated_method_two(self):
        self.logger.debug("Debug decorated_method_two")
        print("This is a decorated method")

if __name__ == "__main__":
    Example2().decorated_method_one()
    Example2().decorated_method_two()
```

This will reproduce

```
$ python example-2.py
DEBUG:__main__:Debug decorated_method_with_name
This is a decorated method
DEBUG:__main__:Debug decorated_method_two
This is a decorated method
```

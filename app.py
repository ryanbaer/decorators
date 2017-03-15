from functools import wraps
import sys, os

class RouteDoesNotExist(Exception):
    pass

class RouteExists(Exception):
    pass
# https://realpython.com/blog/python/primer-on-python-decorators/
# http://scottlobdell.me/2015/04/decorators-arguments-python/
# https://docs.python.org/2/library/functools.html
class App:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def decorator(f):
            if path in self.routes:
                raise RouteExists
            self.routes[path] = f
            @wraps(f)
            def wrapper():
                return f()
            return wrapper
        return decorator

    def request(self, route, *args, **kwargs):
        if route not in self.routes:
            raise RouteDoesNotExist
        self.routes[route]()

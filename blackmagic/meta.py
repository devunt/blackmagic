import inspect
import functools
from time import time


class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        return cls.instances.setdefault(
            cls, super().__call__(*args, **kwargs))


class ProfileMeta(type):
    def __new__(mcs, cls_name, bases, attrs):
        for name, value in attrs.items():
            if inspect.isfunction(value):
                @functools.wraps(value)
                def wrapper(*args, **kwargs):
                    start_ms = time()
                    returned_value = value(*args, **kwargs)
                    end_ms = time()
                    print(f"{cls_name}::{name} elapsed {end_ms - start_ms}ms")
                    return returned_value
                attrs[name] = wrapper
        return super().__new__(mcs, name, bases, attrs)

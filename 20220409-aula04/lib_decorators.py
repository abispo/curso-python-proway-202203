from datetime import datetime
import functools


def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Hora da chamada: {datetime.now()}")
        new_args = list(args)
        new_args[0] = new_args[0] + ' da Silva'
        return func(*new_args, **kwargs)

    return wrapper

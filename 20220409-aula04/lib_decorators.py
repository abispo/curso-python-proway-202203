from datetime import datetime
import functools
from uuid import uuid4
import csv


def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Hora da chamada: {datetime.now()}")
        new_args = list(args)
        new_args[0] = new_args[0] + ' da Silva'
        return func(*new_args, **kwargs)

    return wrapper


def log_function_call(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        fieldnames = ['id', 'name', 'values_list', 'timestamp']

        with open('log_functions.csv', mode='a', newline='') as _file:
            csv_writer = csv.DictWriter(_file, fieldnames=fieldnames, delimiter=';')

            # A função map recebe 2 argumentos: a função que será aplicada a cada item da sequência e a
            # sequência em si
            # A palavra chave lambda serve pra criarmos funções anônimas.

            function_values = map(lambda x: str(x), args)

            data = {
                'id': str(uuid4()),
                'name': func.__name__,
                'values_list': '|'.join(list(function_values)),
                'timestamp': datetime.now().strftime("%Y%m%d%H%H%S")
            }

            if _file.tell() == 0:
                csv_writer.writeheader()

            csv_writer.writerow(data)

            return func(*args, **kwargs)

    return wrapper

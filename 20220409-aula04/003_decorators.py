# decorators
# Decorators é um tipo de recurso que utilizamos para alterar o comportamento padrão de uma função/método/classe
# Funções são considerados objetos de primeira classe, ou seja, podemos passar pra funções, retornar de funções, etc

from lib_decorators import my_decorator


def execute_func(func):
    return func


def hello():
    print("Hello")


def hello2():

    def hello21():
        print("Hello 21")

    def hello22():
        print("Hello 22")

    return hello21


@my_decorator
def decorated_1():
    print("Açúcar sintático")


@my_decorator
def hello_name(name: str, status=False):
    """
    Função que retorna uma mensagem de hello para o usuário
    :param name: str
    :param status: bool
    :return: str
    """
    return f"Hello {name} ({status})"

if __name__ == '__main__':

    # result = execute_func(hello)
    # print(result())
    # print(hello2())

    # hello2() retorna o objeto do tipo function hello21, que por sua vez pode ser chamado logo depois de retornado
    # hello2()()

    # decorated_1()
    # hello_name("João")
    print(hello_name("Maria", False))
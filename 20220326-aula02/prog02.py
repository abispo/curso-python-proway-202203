# Funções

"""
    Função é um bloco de código que é definido em algum lugar do nosso programa, e que pode ser chamado
em qualquer lugar do nosso programa.

    Um função pode ou não receber argumentos (ou parâmetros) e também pode ou não retornar um valor.
    No Python, se não definirmos um valor de retorno para uma função, ela retorna o valor None (Nulo)
    Utilizamos a palavra reservada def para criar uma função.
"""


# hello() imprime uma mensagem no terminal
def hello():
    print("Hello world!")


def hello2():
    return "Hello world!"


# O argumento user é obrigatório
def hello_user(user):
    return f"Hello {user}!"


def add_numbers(number_1, number_2):
    return number_1 + number_2


def show_info(name, info=dict()):
    print(f"Nome: {name}")

    for key, value in info.items():
        print(f"{key} -> {value}")


if __name__ == '__main__':
    x = hello()
    print(x)

    x = hello2()
    print(x)

    print(hello_user("Cristina"))

    print(add_numbers(10, 15))

    # Podemos passar os valores para os argumentos na função pelo seu nome
    # Passando os valores para a função via keyword
    print(add_numbers(number_2=20, number_1=30))

    show_info("Amanda")
    show_info("Amanda", {"class": "Python"})
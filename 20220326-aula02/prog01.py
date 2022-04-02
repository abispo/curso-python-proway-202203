"""

    Dicionários

    Dicionários em Python são uma estrutura de dados do tipo chave: valor. Um dicionário é mutável e iterável.

"""

if __name__ == '__main__':

    # Criando um dicionário
    my_dict = dict()
    my_dict = {"course": "Python", 1.1: True}

    """
    As chaves de um dicionário podem ser dos seguintes tipos:
        - int, str, bool, float
    """

    my_dict = {
        "course": "Python",
        "date": "20220326",
        "students": ["Artur", "Richard"],
        "info": {
            "months": 3,
            "value": 1000.00
        }
    }

    # .update(), .keys(), .values(), .items()

    # Dicionários são estruturas mutáveis, ou seja, podem ter os seus valores alterados
    # Podemos inserir um novo dado em um dicionario de 2 maneiras:
    my_dict["observations"] = "Entry level course"

    # Podemos usar o método update()
    my_dict.update({"observations": "Mid level course"})
    my_dict.update(level=1)

    print(my_dict)

    # Podemos excluir um par chave: valor do nosso dicionário de 3 maneiras:
    # Método pop()
    print(my_dict.pop("level", "Nao existe"))

    # popitem()
    my_dict.update(temp=1)
    print(my_dict)
    print(my_dict.popitem())
    print(my_dict)

    # del
    my_dict.update(temp=1)
    print(my_dict)
    # del my_dict["temp"]
    # print(my_dict)

    # Como Dicionários são tipos de dadds iteráveis, podemos utizá-los dentro de um laço for

    print("="*100)

    my_dict = {
        "name": "Amanda",
        "age": 18,
        "gender": 'F'
    }

    # Dessa maneira, por padrão o Python retorna o nome das chaves desse dicionário
    # Nesse caso, está implícito que o método utilizado é o keys()
    # O comando abaixo é correspondente a for item in my_dict.keys()
    for item in my_dict:
        print(item)

    print(my_dict.keys())

    # Podemos também retornar a lista de valores desse dicionário
    for item in my_dict.values():
        print(item)


    # Podemos também retornar o conjunto chave: valor como uma lista de tuplas
    print(my_dict.items())
    for key, value in my_dict.items():
        print(f"Chave: {key} | Valor: {value}")

    # Podemos deixar o item como uma tupla e depois acessar a chave e o valor pelo índice
    for item in my_dict.items():
        print(f"Chave: {item[0]} | Valor: {item[1]}")
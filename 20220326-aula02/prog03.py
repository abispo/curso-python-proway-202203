
# Funções (continuação)
# Argumentos arbitrários

# Importamos apenas a função calculate_mean do módulo ex01
# from exercicios.ex01 import calculate_mean
from ex01 import calculate_mean


# Podemos fazer tanbém o oposto, que é o empacotamento de valores em um argumento
def calculate_pow_of_sum(*args):
    return sum(args)


def show_log(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


if __name__ == '__main__':

    scores = [10, 10, 9, 9, 9.5]
    print(calculate_mean(scores[0], scores[1], scores[2], scores[3], scores[4]))

    # Podemos passar valores para as funções fazendo o unpacking (desempacotamento) dos argumentos
    print(calculate_mean(*scores))
    # print(calculate_mean(10, 10, 9, 9, 9.5))

    # Podemos também desempacotar os pares chave: valor de dicionários
    scores_dict = {
        "score1": 8,
        "score2": 8.5,
        "score3": 8,
        "score4": 7.5,
        "score5": 9
    }

    result = calculate_mean(**scores_dict)
    print(f"Média: {result:.2f}")

    print(calculate_pow_of_sum(2))
    print(calculate_pow_of_sum(2, 5, 6))
    print(calculate_pow_of_sum())

    machine_01 = {
        "cpu": 87,
        "mem": 2877,
        "fan": True,
    }

    show_log(**machine_01)
    print("*"*50)

    machine_02 = {
        "cpu1": 99,
        "cpu2": 98,
        "mem": 44,
        "disk": 87
    }

    show_log(**machine_02)
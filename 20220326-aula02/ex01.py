"""
Exercício 01

Criar uma função que receberá 5 notas. A função vai ignorar a maior e a menor notas e fazer a média
das 3 notas restantes. Exemplo

calculate_mean(10, 8.5, 7.5, 8, 9)
8.5

"""


def calculate_mean(score1, score2, score3, score4, score5):
    scores = [score1, score2, score3, score4, score5]

    scores.sort()

    # Maneiras
    # scores.pop(-1)
    # scores.pop(0)

    scores = scores[1:4]

    total = sum(scores)
    mean = total / len(scores)

    return mean


if __name__ == '__main__':

    # calculate_mean(lista)
    result = calculate_mean(7, 7.5, 8.5, 8, 8)
    print(f"Resultado: {result:.2f}")
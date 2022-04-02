# Estruturas de controle de repetição.
# Introdução do conceito de listas


if __name__ == '__main__':
    # Listas em Python
    users_list = []     # users_list = list()
    cars_list = ["BMW", "Ferrari", "Masseratti"]
    things_list = [1, 5.6, "Error", [1, 2, 3]]

    # Utilizamos o laço for quando queremos iterar sobre os itens de uma sequência
    for car in cars_list:
        print(car)

    else:
        print("Pronto!")

    # Utizamos while enquanto uma determinada expressão for verdadeira
    # Exemplo de jogo de forca

    word = "Batata"
    user_input = ["", "", "", "", "", ""]
    counter = 0
    max_tries = 10

    while counter <= max_tries:
        char = input("Informe uma letra: ")

        word = word.replace(char, "")

        if len(word) == 0:
            print("Você acertou a palavra!")
            break

        counter += 1
        print(counter)

    else:
        print("Pronto")
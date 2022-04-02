# Exercicio
# Pelo terminal, o usuário vai informar uma lista de itens para compra
# Se o usuário digitar "PRONTO", não serão pedidos mais itens.
# O programa vai listar todos os itens que o usuário forneceu.


if __name__ == '__main__':

    user_input = ""
    object_list = []

    while user_input.upper() != "PRONTO":
        user_input = input("Informe um item para a lista: ")
        object_list.append(user_input)

        # object_list != Object_list

    object_list.pop()

    print("Itens da lista")
    for item in object_list:
        print(item)
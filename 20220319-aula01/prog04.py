# Listas
# Listas são sequências mutáveis e indexáveis

# O índice de uma lista sempre começa por 0

if __name__ == '__main__':

    cars_list = ["Fusca", "Kombi", "Gol", "Chevette", "Variant", "Corcel", "Gurgel"]
    #               0       1       2       3           4
    #               -5      -4      -3      -2          -1

    # Acessando o terceiro item da lista
    print(cars_list[2])
    print(cars_list[-3])

    # Substituindo um item de uma lista pelo seu índice
    cars_list[2] = "Opala"

    print(cars_list)

    cars_list2 = cars_list[:]
    cars_list2.append("Belina")

    print(cars_list)
    print(cars_list2)

    # Usamos slice quando queremos "fatiar" uma sequência (lista, string, etc)
    # Queremos retornar apenas o segundo e terceiro item da lista
    print(cars_list[1:4])

    # 11946099765
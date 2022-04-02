# List Comprehension

if __name__ == '__main__':

    lista = []

    for i in range(1, 11):
        lista.append(i)

    lista2 = [i for i in range(1, 11) if i % 2 == 1]

    print(lista)
    print(lista2)

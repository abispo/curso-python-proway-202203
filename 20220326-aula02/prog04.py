# Trabalhando com arquivos .txt dentro do Python
# Leitura de arquivos
# Utilizamos a função built-in open() para abrir arquivos

if __name__ == '__main__':

    _file = open("prog04_2.txt", mode="r")
    _file.close()


    # Utilizando with, o arquivo é fechado de forma automática quando o bloco de código termina de ser executado
    with open("prog04.txt", mode="r") as _file:

        # O método read lê o conteúdo do arquivo. Podemos especificar a quantidade de caracteres(bytes) que
        # serão lidos
        print(_file.read(10))
        print("\n")
        print(_file.read())

        # Podemos "navegar" no arquivo utilizando os métodos seek() e tell()
        # tell() mostra a posição atual do cursor no arquivo
        print(_file.tell())

        # seek() navega para uma posição específica do arquivo.
        _file.seek(0)
        print(_file.tell())
        print(_file.read())

        print("\n")

        _file.seek(0)

        # O método readline() lê uma linha. Podemos especificar a quantidade de caracteres que serão lidos nessa
        # linha
        print(_file.readline(15))

        _file.seek(0)

        print("\n")

        # O método readlines() retorna as linhas do arquivo como itens de uma lista
        print(_file.readlines())
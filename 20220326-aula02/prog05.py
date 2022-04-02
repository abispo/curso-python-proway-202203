# Trabalhando com arquivos .txt dentro do Python
# Escrita de arquivos
# Utilizamos a função built-in open() para abrir arquivos

from datetime import datetime

if __name__ == '__main__':

    # O modo "w" (escrita) abre um arquivo para escrita. Se esse arquivo não existir, ele é criado. Se esse arquivo existir,
    # o seu conteúdo é sobrescrito
    # O modo "a" (append/adiciobar) abre um arquivo para escrita. Se esse arquivo não existir, ele é criado. Se esse
    # arquivo existir, o novo conteúdo é adicionado ao final do arquivo.
    with open("prog05.txt", mode="w") as _file:

        timestamp = datetime.now().strftime("%Y%m%d %H:%M:%S")
        _file.write(f"{timestamp}\n")

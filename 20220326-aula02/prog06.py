# Trabalhando com arquivos CSV (Comma Separated Value/ Valores separados por vírgula)
# Utilizando csv.reader e csv.writer (listas)

import csv
from uuid import uuid4

if __name__ == '__main__':

    with open("products.csv", mode="r") as _csv_file:

        csv_reader = csv.reader(_csv_file, delimiter=';')

        for row in csv_reader:
            output = f"""
            ID: {row[0]}
            Produto: {row[1]}
            Preço: {row[2]}
            Data: {row[3]}
            {'*'*100}
            """

            print(output)

    # Escrevendo em um arquivo csv

    # O argumento newline evita que na escrita do arquivo .csv, seja inserida uma linha a mais
    with open("users.csv", mode="w", newline='') as _csv_file:

        # fieldnames será a linha com o cabeçalho ou título das colunas
        fieldnames = ["id", "name", "gender"]

        # csv_data é uma lista de listas, que armazena os registros que serão salvos no arquivo .csv
        csv_data = [
            [str(uuid4()), "Amanda", "F"],
            [str(uuid4()), "Carla", "F"],
            [str(uuid4()), "Vanessa", "F"],
            [str(uuid4()), "Bruna", "F"],
            [str(uuid4()), "Elisa", "F"]
        ]

        csv_writer = csv.writer(_csv_file, delimiter=';')

        # Escrevemos o cabeçalho do arquivo
        csv_writer.writerow(fieldnames)

        # writerows recebe uma lista de listas, com cada item dessa lista correspondendo a uma linha no arquivo
        csv_writer.writerows(csv_data)
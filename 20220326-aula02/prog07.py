# Trabalhando com arquivos CSV (Comma Separated Value/ Valores separados por vírgula)
# Utilizando csv.DictReader e csv.DictWriter (listas)

import csv
from uuid import uuid4

if __name__ == '__main__':

    with open("users.csv", mode="r") as _csv_file:
        csv_dict_reader = csv.DictReader(_csv_file, delimiter=';')

        print(csv_dict_reader.fieldnames)

        for row in csv_dict_reader:
            print(row)

    with open("cars.csv", mode="w", newline='') as _csv_file:
        fieldnames = ["id", "model", "year"]
        csv_dict_writer = csv.DictWriter(_csv_file, delimiter=';', fieldnames=fieldnames)

        csv_dict_writer.writeheader()
        csv_dict_writer.writerow({"id": str(uuid4()), "model": "Fusca", "year": "1986"})
        csv_dict_writer.writerow({"id": str(uuid4()), "model": "Brasilia", "year": "1980"})
        csv_dict_writer.writerow({"id": str(uuid4()), "model": "Gol", "year": "1990"})
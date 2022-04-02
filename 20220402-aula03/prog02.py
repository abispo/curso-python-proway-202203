"""
ATM ->      Classe que representa um caixa eletrônico

BankAccount ->  Classe que representa uma conta do cliente
    Atributos:
        - agency            Número da agência
        - number            Número da Conta
        - owner (Client)    Objeto Client que representa o cliente
            - id            id do cliente
            - name          nome do cliente
        - balance           Saldo da conta
        - password          Senha de acesso

    Métodos
        + get_balance()     Retorna o saldo da conta    (Utilizamos @property no lugar)
        + deposit(value)    Realiza um depósito na conta
        + withdraw(value)  Realiza um saque na conta

Client  -> Classe que representa um cliente
    Atributos
        - id                ID único do cliente
        - name              Nome do cliente

    Métodos
        + get_id()          Retorna o ID do cliente
        + get_name()        Retorna o nome do cliente

"""

import csv
from typing import NoReturn

class Client:

    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name


class BankAccount:

    def __init__(self, agency: str, number: str, owner: Client, password: str, balance: float) -> NoReturn:
        self._agency = agency
        self._number = number
        self._owner = owner
        self._password = password
        self._balance = balance

    """
        # Metodo getter
        def get_balance(self):
            return self._balance
        
        # Método setter
        def set_balance(self, value):
            self._balance = value
    """

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    def deposit(self, value):
        self.balance += value
        self._save_account()

    def withdraw(self, value):
        if value <= self.balance:
            self.balance -= value
            self._save_account()
            return self.balance
        else:
            raise Exception

    def _save_account(self):
        _file = open("clients.csv", "r")
        csv_reader = csv.DictReader(_file, delimiter=';')

        data = []
        for client in csv_reader:
            if client.get('id') == self._owner.get_id():
                client['balance'] = self._balance
            data.append(client)

        _file.close()

        _file = open("clients.csv", "w", newline='')
        fieldnames = ["id", "name", "agency", "bank_account", "password", "balance"]
        csv_writer = csv.DictWriter(_file, delimiter=';', fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)

        _file.close()

if __name__ == '__main__':

    agency = input("Informe o número da agência: ")
    bank_account = input("Informe o número da conta: ")
    password = input("Informe a senha: ")

    client = None

    with open("clients.csv", mode="r") as _file:

        dict_reader = csv.DictReader(_file, delimiter=';')

        for item in dict_reader:
            if agency == item.get('agency') \
                    and bank_account == item.get('bank_account') \
                    and item.get('password') == password:
                client = item
                break

    if not client:
        print("Cliente não encontrado!")

    else:

        bank_account = BankAccount(
            client.get('agency'),
            client.get('number'),
            Client(client.get('id'), client.get('name')),
            client.get('password'),
            float(client.get('balance'))
        )

        print("Opções: 1 - Ver saldo | 2 - Fazer depósito | 3 - Fazer saque")
        option = int(input("Informe o que você deseja fazer: "))

        if option == 1:
            print(f"Seu saldo é de {bank_account.balance:.2f}.")

        if option == 2:
            value = float(input("Informe o valor do depósito: "))
            bank_account.deposit(value)

        if option == 3:
            value = float(input("Informe o valor do saque: "))
            bank_account.withdraw(value)

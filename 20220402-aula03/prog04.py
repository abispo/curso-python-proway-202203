
"""
Herança e Polimorfismo

Podemos definir uma classe herdando os atributos e métodos de sua classe pai. Ou seja, tudo que é definido
na classe pai é automaticamente herdado pela classe filha

Vamos modelar um sistema de pagamento
Payment             -> Classe Base
BankslipPayment     -> Classe para pagamentos em boleto bancário
CreditCardPayment   -> Classe para pagamentos usando cartão de crédito
    - Dados necessários: Numero do cartão, codigo, validade, parcelas
BankTransferPayment -> Classe para pagamentos utilizando transferência bancária
    - Dados necessários: Banco, agencia, conta, cpf_titular
"""


class Payment:

    def __init__(self, value: float, description: str = ""):
        self._value = value
        self._description = description

    def pay(self):
        pass


class BankslipPayment(Payment):

    def __init__(self, value: float, barcode: str):
        super().__init__(value=value)
        self._barcode = barcode

    def pay(self):
        return f"Pagamento do boleto '{self._barcode}' no valor de {self._value} efetuado com sucesso."


if __name__ == '__main__':
    bankslip_payment = BankslipPayment(500, "opd8as7r8wegiogpsd8fbawtgdfyadsgfiuagwtdgsfaiu")

    print(bankslip_payment.pay())

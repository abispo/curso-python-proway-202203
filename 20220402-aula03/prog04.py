
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
from datetime import datetime


class Payment:

    def __init__(self, value: float, description: str = ""):
        self._value = value
        self._description = description

    def pay(self):
        pass


class BankslipPayment(Payment):

    def __init__(self, value: float, barcode: str, description: str = ""):
        super().__init__(value=value)
        self._barcode = barcode

    def pay(self):
        return f"Pagamento do boleto '{self._barcode}' no valor de {self._value} efetuado com sucesso."


class CreditCardPayment(Payment):
    def __init__(self, value: float, card_number: str, code: str,
                 valid_thru: datetime, installments: int = 1, description: str = ""):
        super().__init__(value=value, description=description)
        self._card_number = card_number
        self._code = code
        self._valid_thru = valid_thru
        self._installments = installments

    def pay(self):
        output = f"""
        Dados de pagamento:
        ------------------
        Método: Cartão de crédito
        Número do cartão: {self._card_number}
        Valor: {self._value}
        Quantidade de parcelas: {self._installments}
        Valor da parcela: {self._value / self._installments:.2f}
        """
        return output


class BankTransferPayment(Payment):
    def __init__(self, value: float, bank_code: int, agency: str,
                 bank_account: str, document: str, description: str = ""):
        super().__init__(value=value, description=description)
        self._bank_code = bank_code
        self._agency = agency
        self._bank_account = bank_account
        self._document = document

    def pay(self):
        output = f"""
        Dados de pagamento:
        ------------------
        Método: Transferência bancária
        Banco {self._bank_code}
        Número da conta: {self._bank_account}
        Número da agência: {self._agency}
        CPF do titular: {self._document}
        Valor: {self._value}
        """
        return output

if __name__ == '__main__':
    bankslip_payment = BankslipPayment(500, "opd8as7r8wegiogpsd8fbawtgdfyadsgfiuagwtdgsfaiu")
    print(bankslip_payment.pay())

    print("="*50)

    credit_card_payment = CreditCardPayment(878451, "8983-5048-2345-2352-1233", "000", datetime(2028, 10, 1), 6)
    print(credit_card_payment.pay())

    print("="*50)
    bank_transfer_payment = BankTransferPayment(600, 10, "0001", "11111-1", "663748283-19")
    print(bank_transfer_payment.pay())
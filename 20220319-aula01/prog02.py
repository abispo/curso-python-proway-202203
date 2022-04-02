# Calculadora

# O python possui o conceito de tipos de dados. Que são os seguintes:
    # Tipos numéricos (int, float, complex)
    # strings (Tudo que está entre aspas (simples ou duplas)
    # Listas
    # Dicionários
    # Tuplas
    # Sets (Conjuntos)


# O Python possui 3 tipos numéricos.+
#

if __name__ == '__main__':

    # Por padrão, a função input() sempre retorna uma string
    # Portanto, precisamos converter essa string para um tipo numérico (nesse caso, int)
    numero_a = float(input("Informe o primeiro número: "))
    numero_b = float(input("Informe o segundo número: "))
    operacao = input("Informe a operação (+, -, *, /, %, **, //")

    valor = 0

    # if
    # elif
    # else

    if operacao == '+':
        valor = numero_a + numero_b

    elif operacao == '-':
        valor = numero_a - numero_b

    elif operacao == '*':
        valor = numero_a * numero_b

    elif operacao == '/':
        valor = numero_a / numero_b

    elif operacao == '%':
        valor = numero_a % numero_b

    elif operacao == '**':
        valor = numero_a ** numero_b

    else:
        valor = numero_a // numero_b


    print(f"Resultado: {valor}")

    if valor > 10:
        print("Operação realizada com sucesso")

    elif valor <= 10:
        print("Operação falhou")

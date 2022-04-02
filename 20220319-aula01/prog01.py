
# Estrutura de controle de decisão (if, else, elif)
# O sinal == é um operador de comparação

# 1 + 2 * (3 / 4) + 7 -> Exemplo de expressão
# __name__ é uma variável built-in
# __name__ == '__main__' retorna um valor boolean
if __name__ == '__main__':  # True | False
    # Block de código
    print("Ola")

    # A função built-in input() pode receber um valor que irá ser mostrado no terminal
    # Ela retorna o que foi informado pelo usuário no terminal
    # Depois atribuímos esse valor de retorno a variável nome
    # O símbolo = é o operador de atribuição
    nome = input("Informe o seu nome: ")

    # Abaixo nós utilizamos o operador + para fazer a concatenação das strings
    # String é tudo que está dentro de aspas (simples ou duplas)
    print("Olá " + nome)

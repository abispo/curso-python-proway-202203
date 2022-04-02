
# Verificar se o aluno passou de ano
# O script irá receber 3 notas (as notas podem ser do tipo 8.5, 9, etc)
# O script vai calcular a média aritmética dessas notas ( (n1 + n2 + n3) / 3)
# Se a média for menor que 5, mostrar a mensagem "Aluno reprovado"
# Se a média for maior ou igual a 5 E a média for menor do que 7, mostrar a mensagem "Aluno em recuperação
# Se a média for maior ou igual a 7, mostrar a mensagem "Aluno aprovado"

# https://www.w3schools.com/python/python_operators.asp

if __name__ == '__main__':

    n1 = float(input("Informe a primeira nota: "))
    n2 = float(input("Informe a segunda nota: "))
    n3 = float(input("Informe a terceira nota: "))

    media = (n1 + n2 + n3) / 3

    if media < 5:
        # f-strings
        print(f"Aluno reprovado! Média: {media}")

    elif media >= 5 and media < 7:
        print(f"Aluno em recuperação! Média: {media}")

    else:
        print(f"Aluno aprovado! Média: {media}")


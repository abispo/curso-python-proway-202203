# Exceptions

# Exceptions (exceções) são eventos que podem ocorrer no fluxo de execução do nosso código, que fazem o
# programa finalizar.

# try except        Python
# try catch         Javascript, Java, C#, etc

class AuthorizationError(Exception):
    def __init__(self, message, *args, **kwargs):
        self._message = "O usuário não possui acesso"
        super().__init__(message, *args, **kwargs)

    @property
    def message(self):
        return self._message


if __name__ == '__main__':

    try:
        raise AuthorizationError("O usuário não possui permissão para fazer essa operação")

        number_a = int(input("Informe o primeiro número: "))
        number_b = int(input("Informe o segundo número: "))

        result = number_a / number_b

        print(f"O resultado da divisão é {result}.")

    # Podemos informar o tipo de exceção que queremos capturar
    except ZeroDivisionError as error:
        print("Você tentou fazer uma divisão por 0")

    # Podemos ter mais de 1 bloco except
    except ValueError as error:
        print("Valor de entrada incorreto!")

    # Tratando nossa exception personalizada
    except AuthorizationError as error:
        print(f"Erro de Autorização: {error.message}")

    except Exception as error:
        print(f"Erro: {error}")

    # O bloco else é executado apenas se nenhuma exceção for lançada
    else:
        print("Não houveram exceções.")

    # O bloco finally sempre é executado, independentemente se exceções foram lançadas ou não
    finally:
        print("Limpando a sujeira.")

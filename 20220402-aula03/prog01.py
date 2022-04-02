"""
Classes em Python

pikachu = Pokemon("Pikachu", "Elétrico", 70)
----
pikachu = Pokemon()
pikachu.name = "Pikachu"
pikachu.type = "Elétrico"
pikachu.health = 70

"""


class Pokemon:

    """
    O método __init__ serve pra inicializar a nossa classe, ou seja, definir valores de atributos,
    chamar métodos, etc. Pode ser entendido como o correspondente de método construtor em outras linguagens

    """
    def __init__(self, name, pokemon_type, health):
        self._name = name
        self._pokemon_type = pokemon_type
        self._health = health

    def attack(self):
        self.evolve()
        return f"{self._name} atacou com o choque do trovão!"

    def dodge(self):
        return f"{self._name} desviou do ataque!"

    def evolve(self):
        return f"{self._name} evoloiu para Raichu!"


if __name__ == '__main__':
    pikachu = Pokemon("Pikachu", "Elétrico", 70)


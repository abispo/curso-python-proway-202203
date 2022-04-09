# Magic methods (métodos mágicos em Python)

class Number:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def __add__(self, other):
        return self.value + other.value

# Exemplo de utilização de métodos mágicos
# Faremos a classe DeckOfCards se comportar como uma lista


class Card:
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def __repr__(self):
        return f"Card({self.suit} {self.value})"


class DeckOfCards:
    def __init__(self):
        self._cards = []
        self._index = -1

        list_of_suits = ["\u2660", "\u2665", "\u2663", "\u2666"]
        list_of_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for suit in list_of_suits:
            for value in list_of_values:
                self._cards.append(Card(suit, value))

    @property
    def cards(self):
        return self._cards

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index < len(self._cards):
            return self._cards[self._index]

        raise StopIteration


if __name__ == '__main__':

    number_a = Number(10)
    number_b = Number(5)

    print(number_a + number_b)

    deck_of_cards = DeckOfCards()
    # print(deck_of_cards.cards)

    for card in deck_of_cards:
        print(card)

#   metodo(1)
#   object.attribute = 10
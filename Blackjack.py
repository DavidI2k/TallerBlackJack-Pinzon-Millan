class Card:
    def __init__(self,symbol,suit):
        self.cost=symbol
        self.symbol = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][symbol-1]
        self.suit = '♥♦♣♠'[suit]

    def mostrar(self):
        print('┌───────┐')
        print(f'| {self.symbol:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.symbol:>2} |')
        print('└───────┘') 

    def puntaje(self):
        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost

import random
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

class Dealer:
    def __init__(self):
        self.deck = []

    def generate(self):
        for i in range(1, 14):
            for j in range(4):
                self.deck.append(Card(i, j))
    
    def Randomize(self, iteration):
        deck = []
        for i in range(iteration):
            card = random.choice(self.deck)
            self.deck.remove(card)
            deck.append(card)
        return deck

    def count(self):
        return len(self.deck)

class Player:
    def __init__(self, isDealer, cards):
        self.deck = []
        self.isDealer = isDealer
        self.cards= cards
        self.score = 0

    def AddCard(self):
        self.deck.extend(self.cards.draw(1))
        self.check_score()
        if self.score > 21:
            return 1
        return 0

    def deal(self):
        self.deck.extend(self.cards.draw(2))
        self.check_score()
        if self.score == 21:
            return 1
        return 0

    def mirar_puntaje(self):
        a_counter = 0
        self.score = 0
        for card in self.deck:
            if card.price() == 11:
                a_counter += 1
            self.score += card.price()

        while a_counter != 0 and self.score > 21:
            a_counter -= 1
            self.score -= 10
        return self.score

    def Mostrar(self):
        if self.isDealer:
            print("Cartas del Dealer")
        else:
            print("Cartas del Jugador")

        for i in self.deck:
            i.Mostrar()

        print("Puntaje: " + str(self.score))
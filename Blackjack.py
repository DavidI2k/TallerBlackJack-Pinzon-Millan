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
        self.deck.extend(self.cards.Randomize(1))
        self.mirar_puntaje()
        if self.score > 21:
            return 1
        return 0

    def deal(self):
        self.deck.extend(self.cards.Randomize(2))
        self.mirar_puntaje()
        if self.score == 21:
            return 1
        return 0

    def mirar_puntaje(self):
        a_counter = 0
        self.score = 0
        for card in self.deck:
            if card.puntaje() == 11:
                a_counter += 1
            self.score += card.puntaje()

        while a_counter != 0 and self.score > 21:
            a_counter -= 1
            self.score -= 10
        return self.score

    def mostrar(self):
        if self.isDealer:
            print("Cartas del Dealer")
        else:
            print("Cartas del Jugador")

        for i in self.deck:
            i.mostrar()

        print("Puntaje: " + str(self.score))

class Juego:
    def __init__(self):
        self.cards = Dealer()
        self.cards.generate()
        self.player = Player(False, self.cards)
        self.dealer = Player(True, self.cards)

    def play(self):
        p_status = self.player.deal()
        d_status = self.dealer.deal()

        self.player.mostrar()

        if p_status == 1:
            print("¡El jugador obtuvo Blackjack, Felicidades!")
            if d_status == 1:
                print("¡El jugador y el Dealer obtuvieron Blackjack! Es un empate.")
            return 1

        cmd = ""
        while cmd != "Mantener":
            bust = 0
            cmd = input("Pedir o Mantener? ")

            if cmd == "Pedir":
                bust = self.player.AddCard()
                self.player.mostrar()
            if bust == 1:
                print("El jugador se pasó. Buen juego!")
                return 1
        print("\n")
        self.dealer.mostrar()
        if d_status == 1:
            print("¡El Dealer obtuvo Blackjack, mejor suerte la próxima!")
            return 1

        while self.dealer.mirar_puntaje() < 17:
            if self.dealer.AddCard() == 1:
                self.dealer.mostrar()
                print("¡El Dealer de pasó. Felicidades!")
                return 1
            self.dealer.mostrar()

        if self.dealer.mirar_puntaje() == self.player.mirar_puntaje():
            print("¡Es un empate, mejor suerte la próxima!")
        elif self.dealer.mirar_puntaje() > self.player.mirar_puntaje():
            print("¡El repartidor gana, buen juego!")
        elif self.dealer.mirar_puntaje() < self.player.mirar_puntaje():
            print("¡El jugador gana, felicidades!")

b = Juego()
b.play()

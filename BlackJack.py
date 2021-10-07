from ctypes import alignment
from tkinter import *
import tkinter
import sys
import os
from tkinter import font
from typing import Collection

ventana = Tk()
ventana.title("Black Jack")
ventana.geometry("450x150")
ventana.configure(bg="green")

cont_dealer = 0
cont_jugador = 0
global PGdlr
global PGjgd
PGdlr = Label(ventana,text=cont_dealer)
PGjgd = Label(ventana,text=cont_jugador)
PGdlr.grid(row= 2, column=1)
PGjgd.grid(row=3, column=1)

import random
class Card:
    def __init__(self,symbol,suit):
        self.valor = symbol
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
        if self.valor >= 10:
            return 10
        elif self.valor == 1:
            return 11
        return self.valor




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
        if self.score >= 21:
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
    def __init__(self,master):
        self.cards = Dealer()
        self.cards.generate()
        self.player = Player(False, self.cards)
        self.dealer = Player(True, self.cards)
        self.BotonM= Button(ventana,text="Mantener",command=self.Mantenga,borderwidth=4, )
        self.BotonP= Button(ventana,text="Pedir",command=self.Pida,borderwidth=4)
        self.botonN= Button(ventana,text="Nuevo Juego",command=self.Nuevo,borderwidth=4)
        self.blank = Label(ventana, text="                                                  ", bg="green")
        self.tit = Label(ventana,text="Bienvenido a BlackJack",font="Helvetica",bg="#27c471")
        self.BotonM.grid(row=2,column=4)
        self.BotonP.grid(row=3,column=4)
        self.botonN.grid(row=4,column=4)
        self.blank.grid(row=1,column=1)
        self.tit.grid(row=0,column=4)

    

    def Pida(self):
        global cont_jugador
        global cont_dealer



        print("\n")
        self.player.AddCard()
        self.player.mostrar()




        if self.dealer.mirar_puntaje() == self.player.mirar_puntaje():
            print("El repartidor gana, buen juego!")
            cont_dealer += 1
        elif self.player.mirar_puntaje() == 21:
            print("¡El jugador gana, felicidades!")
            cont_jugador += 1
        elif self.dealer.mirar_puntaje() == 21:
            print("¡El repartidor gana, buen juego!")
            cont_dealer += 1
        elif self.dealer.mirar_puntaje() < self.player.mirar_puntaje() and self.player.mirar_puntaje() > 21:
            print("¡El repartidor gana, buen juego!")
            cont_dealer += 1
        elif self.dealer.mirar_puntaje() > self.player.mirar_puntaje() and self.dealer.mirar_puntaje() > 21:
            print("¡El jugador gana, felicidades!")
            cont_jugador += 1

        
    def Mantenga(self):
        global cont_dealer
        global cont_jugador

        d_status = self.dealer.deal()
        print("\n")
        self.dealer.mostrar()
        if d_status == 1:
            print("¡El Dealer obtuvo Blackjack, mejor suerte la próxima!")
            cont_dealer += 1
            return 1
        while self.dealer.mirar_puntaje() < 17:
            if self.dealer.AddCard() == 1:
                self.dealer.mostrar()
                print("¡El Dealer se pasó. Felicidades!")
                cont_jugador += 1
                return 1
            self.dealer.mostrar()

        if self.dealer.mirar_puntaje() == self.player.mirar_puntaje():
            print("El repartidor gana, buen juego!")
            cont_dealer += 1
        elif self.player.mirar_puntaje() == 21:
            print("¡El jugador gana, felicidades!")
            cont_jugador += 1
        elif self.dealer.mirar_puntaje() == 21:
            print("¡El repartidor gana, buen juego!")
            cont_dealer += 1
        elif self.dealer.mirar_puntaje() < self.player.mirar_puntaje() and self.player.mirar_puntaje() > 21:
            print("¡El repartidor gana, buen juego!")
            cont_dealer += 1
        elif self.dealer.mirar_puntaje() > self.player.mirar_puntaje() and self.dealer.mirar_puntaje() > 21:
            print("¡El jugador gana, felicidades!")
            cont_jugador += 1

    def play(self):
        global cont_dealer
        global cont_jugador
        p_status = self.player.deal()
        d_status = self.dealer.deal()

        self.player.mostrar()

        if p_status == 1:
            print("¡El jugador obtuvo Blackjack, Felicidades!")
            cont_jugador += 1
            if d_status == 1:
                print("¡El jugador y el Dealer obtuvieron Blackjack! Es un empate.")
            return 1
        print("\n")
        self.dealer.mostrar()
        if d_status == 1:
            print("¡El Dealer obtuvo Blackjack, mejor suerte la próxima!")
            cont_dealer += 1
            return 1



    def Nuevo(self):
        global cont_dealer
        global cont_jugador
        python = sys.executable
        os.execl(python,python, * sys.argv)
        



b = Juego(ventana)
b.play()
ventana.mainloop()
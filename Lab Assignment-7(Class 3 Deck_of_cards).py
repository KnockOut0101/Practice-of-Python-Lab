import random

class card:
    def __init__(self,suit,value):
        self.card_suit=suit
        self.card_value = value

    def create_card(self):
        self.card_object = [self.card_suit,self.card_value]
        return self.card_object


class Deck:
    def __init__(self):
        self.suit = ["Hearts","Spades","Diamonds","Clubs"]
        self.values = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    def create_deck(self):
        self.deck=[]
        for i in range(len(self.suit)):
            for j in range(len(self.values)):
                Unique_card = card(self.suit[i],self.values[j])
                Unique_card = Unique_card.create_card()
                self.deck.append(Unique_card)
        return self.deck

    def deal(self):
        self.deck = self.deck[:-1]
        return self.deck



deck = Deck()

deck_of_cards = deck.create_deck()

print(deck_of_cards)

deck_of_cards = deck.deal()

print(deck_of_cards)

#random.shuffle(deck)

#print(deck)
from card import Card

from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                self.add_card(Card(suit, rank))
        self.shuffle()        

    def __str__(self):
        i=1
        string=""
        for card in self.cards:
            string+=f"{str(card)} |"    
            i+=1        
        return string

    def __len__(self):
        return len(self.cards)  

    
    def add_card(self,card):
        self.cards.append(card)

    def pop_card(self):
        if len(self.cards):
            return self.cards.pop(0)

    def shuffle(self):
        shuffle(self.cards)   









        


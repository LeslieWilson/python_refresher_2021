import random

class Card:
    def __init__(self, num, suite, value, altvalue):
        self.suite = suite
        self.num = num
        self.value = value
        self.altvalue = altvalue
    
    def __repr__(self):
        return "Card(" + str(self.suite) + "," + str(self.num) + "," + str(self.value) + "," + str(self.altvalue) + ")"

    def __str__(self):
        if self.num == 1:
            return "ace of" + self.suite
        elif self.num == 11:
            return "jack of" + self.suite
        elif self.num == 12:
            return "queen of" + self.suite
        elif self.num == 13:
            return "king of" + self.suite
        else:
            return str(self.num) + " " + self.suite



class Deck:
    def __init__(self):
        self.cards = []
        self.generate_deck()
        self.shuffle()

    def generate_deck(self):
        for suite in ["hearts", "clubs", "spades", "diamonds", ]:
            for num in range(1,14):
                card = Card(num, suite,num,num)
                if card.num == 1:
                    card.altvalue = 11
                if card.num == 11:
                    card.value = 10
                    card.altvalue = 10
                if card.num == 12:
                    card.value = 10
                    card.altvalue = 10
                if card.num == 13:
                    card.value = 10
                    card.altvalue = 10
                self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)

    def __getitem__(self,i):
        return self.cards[1]

    


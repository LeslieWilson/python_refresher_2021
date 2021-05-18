class Card:
    def __init__(self):
        self.suite = "Heart"
        self.num = 1
        self.value = 1
        self.altvalue = 11
    def __str__(self):
        if self.num == 1:
            return "ace of" + suit
        elif self.num == 11:
            return "jack of" = suit
        elif self.num == 12:
            return "queen of" = suit
        elif self.num == 13:
            return "king of" = suit
        else:
            return str(num) + " " + suit
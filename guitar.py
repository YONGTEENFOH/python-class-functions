class guitar:
    def __init__(self, name, price, quality):
        self.name = name
        self.price = price
        self.quality = quality

#functions created to find the best value guitar
    def less_than_RM200_and_good(self):
        if self.price <= 200 and self.quality == "good":
            return True
        else:
            return False
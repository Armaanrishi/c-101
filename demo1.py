class Bank:
    def __init__(self,AtmCardNumber,PinNumber):
        self.AtmCardNumber = AtmCardNumber
        self.PinNumber = PinNumber

    def details(self):
        print(self.AtmCardNumber,self.PinNumber)

HDFC  = Bank("9876543210","2345")
HDFC.details()

ICICI = Bank("1234567890","9876")
ICICI.details()

   
#definine variables
hits = 10.000
atBats = 30.000
#define functions
def printWhatsUp():
    print("What's up doc!")

def battingAverage():
    print 'Your batting average is ', (hits/atBats)
    
#define a class
class baseballBat:
    def __init__(self):
        self.make = raw_input("What brand is the baseballBat?")
        self.model = raw_input("What model is the baseballBat?")
        self.price = raw_input("What price is the baseballBat?")

    def printdetails(self):
        print("This bat is a " + self.make + self.model)
        print("This bat cost " + self.price + " dollars.")

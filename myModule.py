age = 14
weight = 100

def printGoodbye():
    print("Goodbye!")

def dogYears(age):
    print(age * 7)

class Car:
    def __init__(self):
        self.make = raw_input("What make is the car?")
        self.model = raw_input("What model is the car?")
        self.price = raw_input("What price is the car?")

    def printdetails(self):
        print("This car is a " + self.make + self.model)
        print("This car cost " + self.price + "dollars.")

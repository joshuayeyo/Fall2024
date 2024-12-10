from random import randint

class Dice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__value = 1
        self.__size = 30

    def readDice(self):
        return self.__value

    def printDice(self):
        print("주사위의 값> ", self.__value)

    def rollDice(self):
        self.__value = randint(1, 6)

d = Dice(100, 100)
d.rollDice()
d.printDice()

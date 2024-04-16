# Part a)
class Balloon():
    # Health int
    # DefenceItem str
    # Colour str
    def __init__(self, DefenseItem, Colour):
        self.__Health = 100
        self.__DefenceItem = DefenseItem
        self.__Colour = Colour

    # Part b)
    def GetDefenceItem(self):
        return self.__DefenceItem
    
    # Part c)
    def ChangeHealth(self, Change):
        self.Health = self.__Health + Change

    # Part d)
    def CheckHealth(self):
        if self.Health <= 0:
            return True
        else:
            return False

# Part e)
defenceitem = input("Enter a Defence Item: ")
Colour = input("Enter a Colour: ")

Balloon1 = Balloon(defenceitem, Colour)

# Part f)
def Defend(balloon):
    strength = int(input("Enter Strength value: "))
    balloon.ChangeHealth(-strength)
    print(balloon.GetDefenceItem)

    if balloon.CheckHealth() == True:
        print(f"Balloon has no health.")
    elif balloon.CheckHealth() == False:
        print(f"Balloon has health.")

    return balloon

Defend(Balloon1)
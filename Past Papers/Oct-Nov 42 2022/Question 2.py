class Character():
    def __init__(self, Name, XCoordinate, YCoordinate):
        self.Name = Name
        self.XCoordinate = XCoordinate
        self.YCoordinate = YCoordinate

    def GetName(self):
        return self.Name
    
    def GetX(self):
        return self.XCoordinate
    
    def GetY(self):
        return self.YCoordinate
    
    def ChangePosition(self, XChange, YChange):
        self.XCoordinate = self.XCoordinate + XChange
        self.YCoordinate = self.YCoordinate + YChange

CharArray = [0 for x in range(10)]
with open('D:/Coding/Repos/A-Levels/Past Papers/Oct-Nov 42 2022/Papers/Characters.txt', 'r') as Doc:
    for i in range(10):
        name = Doc.readline().rstrip('\n').lower()
        x = int(Doc.readline())
        y = int(Doc.readline())
        CharArray[i] = Character(name, x, y)

Found = False
while Found == False:
    SearchFor = input("Enter a character name: ").lower()
    for x in range(10):
        if CharArray[x].GetName() == SearchFor:
            FoundAt = x
            Found = True

Move = input("Enter a direction: ")
while True:
    match Move:
        case 'A':
            CharArray[FoundAt].ChangePosition(-1, 0)
            break
        case 'W':
            CharArray[FoundAt].ChangePosition(0, 1)
            break
        case 'S':
            CharArray[FoundAt].ChangePosition(0, -1)
            break
        case 'D':
            CharArray[FoundAt].ChangePosition(1, 0)
            break
        case _:
            Move = input("Try Again: ")

Player = CharArray[FoundAt]

print(f"{Player.GetName()} has changed coordinates to x = {Player.GetX()} and Y = {Player.GetY()}")
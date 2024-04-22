# Part a)
class Picture():
    def __init__(self, Description, Width, Height, FrameColour):
        self.__Description = Description
        self.__Width = Width
        self.__Height = Height
        self.__FrameColour = FrameColour

    def GetDescription(self):
        return self.__Description
    
    def GetHeight(self):
        return int(self.__Height)
    
    def GetWidth(self):
        return int(self.__Width)
    
    def GetColour(self):
        return self.__FrameColour
    
    def SetDescription(self, Description):
        self.__Description = Description

PicArray = [] # Type: Picture, Elements: 100

def ReadData():
    global PicArray
    try:
        with open('Repos/A-Levels/Past Papers/Oct-Nov 42 2021/Papers/Pictures.txt', 'r') as Doc:
            for x in range(21):
                desc = str(Doc.readline()).rstrip('\n')
                width = int(Doc.readline())
                height = int(Doc.readline())
                framecolour = str(Doc.readline()).rstrip('\n')
                MyPicture = Picture(desc, width, height, framecolour)
                PicArray.append(MyPicture)

    except FileNotFoundError:
        print("File Not Found")

ReadData()

UserColour = input("Enter Colour: ").lower()
UserMaxWidth = int(input("Enter Max Width: "))
UserMaxHeight = int(input("Enter Max Height: "))

for Pic in PicArray:
    ToCheck = Pic
    if (UserMaxHeight >= ToCheck.GetHeight()) and (UserMaxWidth >= ToCheck.GetWidth()) and (UserColour == ToCheck.GetColour()):
        print(f"Picture Description: {ToCheck.GetDescription()}, PictureWidth: {ToCheck.GetWidth()}, Picture Height: {ToCheck.GetHeight()}")
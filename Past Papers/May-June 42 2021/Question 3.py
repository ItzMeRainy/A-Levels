# Part a)
class TreasureChest():
    def __init__(self, question, answer, points):
        self.__question = question # string
        self.__answer = answer # int
        self.__points = points # int

    # Part c) (i)
    def getQuestion(self):
        return self.__question
    
    # Part c) (ii)
    def checkAnswer(self, UserAnswer):
        if UserAnswer == self.__answer:
            return True
        else:
            return False
        
    # Part c) (iii)
    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2
        elif attempts in [3, 4]:
            return self.__points // 4
        elif attempts > 4:
            return 0

# Part b)
def readData():
    global arrayTreasure
    arrayTreasure = []
    try:
        with open('Repos/A-Levels/Past Papers/May-June 42 2021/Papers/TreasureChestData.txt', 'r') as Doc:
            for x in range(5):
                question = Doc.readline()
                answer = int(Doc.readline())
                points = int(Doc.readline())
                arrayTreasure.append(TreasureChest(question, answer, points))
    except FileNotFoundError:
        print("File Not Found")

# Part c) (iv)
readData()

questionNumber = int(input("Enter Question Number: ")) - 1

ThisQuestion = arrayTreasure[questionNumber]

print(ThisQuestion.getQuestion())
answer = int(input("Your Answer? "))

count = 1

answer = 0
while ThisQuestion.checkAnswer(answer) == False:
    answer = int(input("Try Again: "))
    count += 1

Total = ThisQuestion.getPoints(count)
print(f"{Total} is your points.")
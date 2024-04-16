# Part a)
global ScoreArray
ScoreArray = [['']*2 for x in range(11)]

# Part b)
def ReadHighScores():
    global ScoreArray
    try:
        with open('Repos\A-Levels\Past Papers\May-June 41 2022\Papers\HighScore.txt', 'r') as Doc:
            for x in range(10):
                ScoreArray[x][0] = Doc.readline().rstrip('\n')
                ScoreArray[x][1] = int(Doc.readline().rstrip('\n'))
    except IOError:
        print("File Not Found")

# Part c)
def OutputHighScores():
    for x in range(len(ScoreArray)):
        Combined = f"{ScoreArray[x][0]} {ScoreArray[x][1]}"
        print(Combined)

# Part d)
ReadHighScores()
OutputHighScores()

# Part e)
while True:
    Username = input("Enter Username: ")
    if len(Username) == 3:
        break
while True:
    UserScore = int(input("Enter Score: "))
    if UserScore >= 1 and UserScore <= 100_000:
        break

def PlaceScore(Name, Score):
    ScoreArray[10][0] = Name
    ScoreArray[10][1] = Score
    for j in range(len(ScoreArray) - 1):
        for i in range(len(ScoreArray) - 1):
            if ScoreArray[i][1] < ScoreArray[i + 1][1]:
                ScoreArray[i], ScoreArray[i + 1] = ScoreArray[i + 1], ScoreArray[i]

PlaceScore(Username, UserScore)

# Part f)
def WriteTopTen():
        with open('Repos/A-Levels/Past Papers/May-June 41 2022/Papers/NewHighScore.txt', 'a') as File:
            for user in ScoreArray:
                File.write(f"{user[0]}\n")
                File.write(f"{user[1]}\n")

WriteTopTen()
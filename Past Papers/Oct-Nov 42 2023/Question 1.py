global StackVowel
global StackConsonant
StackVowel = [0 for x in range(100)] # Array, Type: String, of 100 elements
StackConsonant = [0 for x in range(100)] # Array, Type: String, of 100 elements

global VowelTop, ConsonantTop
VowelTop = 0
ConsonantTop = 0

def PushData(alph):
        global StackVowel, StackConsonant, VowelTop, ConsonantTop
        if alph in ["a", "e", "i", "o", "u"]:
            if VowelTop <= 100:
                StackVowel[VowelTop] = alph
                VowelTop += 1
            else:
                print("Stack Full! (Vowel)")
        else:
            if ConsonantTop <= 100:
                StackConsonant[ConsonantTop] = alph
                ConsonantTop += 1
            else:
                print("Stack Full! (Consonant)")

def ReadData():
    try:
        with open('Repos/A-Levels/Past Papers/Oct-Nov 42 2023/Papers/StackData.txt', 'r') as Doc:
            for x in range(100):
                ThisAlph = Doc.readline().rstrip('\n')
                PushData(ThisAlph)
    except FileNotFoundError:
        print("File Not Found.")

def PopVowel():
    global StackVowel, VowelTop
    if VowelTop <= -1:
        return "No Data"
    else:
        ToReturn = StackVowel[VowelTop - 1]
        StackVowel[VowelTop - 1] = 0
        VowelTop -= 1
        return ToReturn

def PopConsonant():
    global StackConsonant, ConsonantTop
    if ConsonantTop <= -1:
        return "No Data"
    else:
        ToReturn = StackConsonant[ConsonantTop - 1]
        StackConsonant[ConsonantTop - 1] = 0
        ConsonantTop -= 1
        return ToReturn

ReadData()

UserString = ''
for x in range(5):
    Choice = input("Vowel or Consonant? ")
    if Choice == "vowel":
        ToAdd = PopVowel()
    elif Choice == "consonant":
        ToAdd = PopConsonant()
    if ToAdd == "No Data":
        print("Stack was empty.")
        ToAdd = ''
    UserString += ToAdd

print(UserString)
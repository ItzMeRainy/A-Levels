# Part a)
global Animals 
Animals = [] #array 10 elements string

# Part b)
Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")

# Part C)
def SortDescending():
    ArrayLength = 0 # Type: Integer
    Temp = "" # Type: String
    ArrayLength = len(Animals)

    for X in range(ArrayLength - 1):
        for Y in range(ArrayLength - X - 1):
            if Animals[Y][0:1] < Animals[Y+1][0:1]:
                Animals[Y], Animals[Y+1] = Animals[Y+1], Animals[Y]

# Part d)
SortDescending()
for Animal in Animals:
    print(Animal)
# Part a)
global arrayData
arrayData = [] # array, 10 elements, int
arrayData.append(10)
arrayData.append(5)
arrayData.append(6)
arrayData.append(7)
arrayData.append(1)
arrayData.append(12)
arrayData.append(13)
arrayData.append(15)
arrayData.append(21)
arrayData.append(8)
print(arrayData)

# Part b)
def linearSearch(num):
    for number in arrayData:
        if number == num:
            return True
    return False

NumEntered = int(input("Enter Number to Search: "))
status = linearSearch(NumEntered)
print("Found") if status == True else print("Not Found")

# Part c)
def bubbleSort(theArray):
    temp = 0 # int
    for x in range(len(theArray)):
        for y in range(len(theArray) - 1):
            if theArray[y] < theArray[y + 1]:
                temp = theArray[y]
                theArray[y] = theArray[y + 1]
                theArray[y + 1] = temp
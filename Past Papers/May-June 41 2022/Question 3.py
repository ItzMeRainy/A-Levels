# Part a)
QueueArray = [0 for x in range(10)] # Array string of 10 items
Headpointer = 0 # Type: Integer
Tailpointer = 0 # Type: Integer
Numitems = 0 # Type: Integer

# Part b)
def Enqueue(QueueArray, HeadPointer, TailPointer, NumItems, Data):
    if NumItems == 10:
        return (False, QueueArray, TailPointer, NumItems)
    QueueArray[TailPointer] = Data
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer += 1
    NumItems += 1
    return (True, QueueArray, TailPointer, NumItems)

# Part c)
def Dequeue(QueueArray, HeadPointer, TailPointer, NumItems):
    if NumItems == 0:
        return (False, QueueArray, HeadPointer, NumItems)
    else:
        ToReturn = QueueArray[HeadPointer]
    if HeadPointer >= 9:
        HeadPointer = 0
    else:
        HeadPointer += 1
    NumItems -= 1
    return (ToReturn, QueueArray, HeadPointer, NumItems)

# Part d)
for x in range(11):
    Data = input("Enter your data: ")
    Status, QueueArray, Tailpointer, Numitems = Enqueue(QueueArray, Headpointer, Tailpointer, Numitems, Data)
    if Status == True:
        print("Added")
    else:
        print("Unsuccessful")

Result, QueueArray, Headpointer, Numitems = Dequeue(QueueArray, Headpointer, Tailpointer, Numitems)
print(Result)
Result, QueueArray, Headpointer, Numitems = Dequeue(QueueArray, Headpointer, Tailpointer, Numitems)
print(Result)
# Part a)
class LinkedListNode():
    def __init__(self, Data, NextNode):
        self.Data = Data
        self.NextNode = NextNode

# Part b)
LinkedList = [] # array of type node

LinkedList.append(LinkedListNode(1, 1))
LinkedList.append(LinkedListNode(5, 4))
LinkedList.append(LinkedListNode(6, 7))
LinkedList.append(LinkedListNode(7, -1))
LinkedList.append(LinkedListNode(2, 2))
LinkedList.append(LinkedListNode(0, 6))
LinkedList.append(LinkedListNode(0, 8))
LinkedList.append(LinkedListNode(56, 3))
LinkedList.append(LinkedListNode(0, 9))
LinkedList.append(LinkedListNode(0, -1))

startPointer = 0 # int
emptyPointer = 5 # int

# Part c)
def outputNodes(array , currentpointer):
    while currentpointer != -1:
        print(array[currentpointer].Data)
        currentpointer = array[currentpointer].NextNode

outputNodes(LinkedList, startPointer)

# Part d)
def addNode(linkedList, currentPointer, emptyList): 
    dataToAdd = input("Enter the data to add: ")

    if emptyList <0 or emptyList > 9:
        return False
    else:
        linkedList[emptyList] = LinkedListNode(int(dataToAdd), -1)
         
        previousPointer = 0

        while currentPointer != -1:
            previousPointer = currentPointer
            currentPointer = linkedList[currentPointer].NextNode

        linkedList[previousPointer].NextNode = emptyList
        emptyList = linkedList[emptyList].NextNode

        return True

status = addNode(LinkedList, startPointer, emptyPointer)
if status == True:
    print("Added")
else:
    print("Not Added")

outputNodes(LinkedList, startPointer)
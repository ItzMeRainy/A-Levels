# Part a)
class SaleData():
    def __init__(self, ID, Quantity):
        self.ID = ID
        self.Quantity = Quantity
    def __repr__(self):
        return f"{self.ID} + {self.Quantity}"

# Part b)
global CircularQueue, Head, Tail, NumberOfItems

CircularQueue = [SaleData("", -1) for x in range(5)]
Head = 0 #int
Tail = 0 #int
NumberOfItems = 0 #int

# Part c)
def Enqueue(SaleDataRecord):
    global Tail, CircularQueue, NumberOfItems
    if NumberOfItems > 4:
        return -1
    else:
        CircularQueue[Tail] = SaleDataRecord
        Tail += 1
        NumberOfItems += 1

        if Tail == 5:
            Tail = 0
        
        return 1

# Part d)   
def Dequeue():
    global Head, CircularQueue, NumberOfItems
    if NumberOfItems < 1:
        return SaleData("", -1)
    else:
        ToReturn = CircularQueue[Head]
        Head += 1
        NumberOfItems -= 1
        if Head == 4:
            Head = 0
        return ToReturn
    
# Part e)
def EnterRecord(ID, Quantity):
    ID = str(ID)
    ToEnter = SaleData(ID, Quantity)

    status = Enqueue(ToEnter)
    if status == -1:
        print("Full")
    else:
        print("Stored")

# Part f)
EnterRecord("ADF", 10)
EnterRecord("OOP", 1)
EnterRecord("BXW", 5)
EnterRecord("XXZ", 22)
EnterRecord("HQR", 6)
EnterRecord("LLP", 3)

Result = Dequeue()
if Result.ID == "":
    print("Queue Empty")
else:
    print(Result.ID)

EnterRecord("LLP", 3)

for Data in CircularQueue:
    print(f"{Data.ID} and {Data.Quantity}")
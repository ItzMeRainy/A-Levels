ArrayNodes = [[0 for x in range(3)] for x in range(20)]
RootPointer = -1
FreeNode = 0

def AddNode():
    global ArrayNodes, RootPointer, FreeNode
    NodeData = int(input("Enter the data"))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode += 1
    else:
        print("Tree is Full")

def PrintAll():
    for Node in ArrayNodes:
        print(f"{Node[0]}, {Node[1]}, {Node[2]}")

for x in range(10):
    AddNode()
PrintAll()

def InOrder(RootPointer):
    if ArrayNodes[RootPointer][0] != -1:
        InOrder(ArrayNodes[RootPointer][0])

    print(ArrayNodes[RootPointer][1])

    if ArrayNodes[RootPointer][2] != -1:
        InOrder(ArrayNodes[RootPointer][2])
InOrder(RootPointer)
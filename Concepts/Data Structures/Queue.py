Queue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]                 # 10 element queue, defined and initialized.
QueueLength = len(Queue)                               # Assigned to see how many spaces are available in queue.
TailPointer = 0                                        # Elements added are sent to the back or the tail of the queue.
HeadPointer = 0                                        # Elements removed are dequeued from the beginning or head of the queue.
Entries = 0                                            # Represents total number of elements currently present in queue.

# Procedure to add number to queue.
def Enqueue():
    global TailPointer, Entries
    num = int(input("Enter number to add: "))
    if Entries < QueueLength:
        if TailPointer >= QueueLength:
            TailPointer = 0
        Queue[TailPointer] = num
        TailPointer += 1
        Entries += 1
    else:
        print("Queue is Full")

# Procedure to remove number from queue.
def Dequeue():
    global HeadPointer, Entries
    if Entries > 0:
        if HeadPointer >= QueueLength:
            HeadPointer = 0
        Queue[HeadPointer] = 0
        HeadPointer += 1
        Entries -= 1
    else:
        print("Queue is Empty")

# Note: This queue is circular.

print(Queue)
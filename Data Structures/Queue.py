Queue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 10 element queue, defined and initialized.
QueueLength = len(Queue) # Assigned to see how many spaces are available in queue.
TailPointer = 0 # Elements added are sent to the back or the tail of the queue.
HeadPointer = 0 # Elements removed are dequeued from the beginning or head of the queue.
Entries = 0 # Represents total number of elements currently present in queue.

# Method to add number to queue.
def Enqueue():
    global TailPointer, Entries
    num = int(input("Enter number to add: "))
    if TailPointer >= QueueLength - 1:
        TailPointer = 0
    if Entries < QueueLength - 1:
        Queue[TailPointer] = num
        TailPointer += 1
        Entries += 1
    else:
        print("Queue is Full")

# Method to remove number from queue.
def Dequeue():
    global HeadPointer, Entries
    if HeadPointer >= QueueLength - 1:
        HeadPointer = 0
    if Entries > 0:
        Queue[HeadPointer] = 0
        HeadPointer += 1
        Entries -= 1
    else:
        print("Queue is Empty")

# Note: This queue is circular.
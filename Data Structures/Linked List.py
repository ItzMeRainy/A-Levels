# Creating class for Nodes, for the elements in the linked list.
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    # No need to learn this (Makes it possible to print the object).
    def __repr__(self):
        return self.value

# Creating wrapper class for the ListNode class.
class LinkedList:
    def __init__(self):
        self.head = None

    # No need to learn this (Makes it possible to print the object).
    def __repr__(self):
        node = self.head
        nodes = []
        while node != None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # Append method to add node to the end of the linked list.
    def Append(self, value):
        NewNode = ListNode(value)
        
        # Case for empty list.
        if self.head == None:
            self.head = NewNode

        # Case for if list is not empty: Jumps from one memory address to next until it reaches "None" and overwrites it with the Node to be added.
        else:
            CurrentNode = self.head
            while CurrentNode.next != None:
                CurrentNode = CurrentNode.next
            
            CurrentNode.next = NewNode

    # Helper method to be used for error checking for the Delete() function (Checks the length of the linked list).
    def LengthLinkedList(self):
        CurrentNode = self.head
        Counter = 0
        while CurrentNode != None:
            CurrentNode = CurrentNode.next
            Counter += 1
        return Counter

    # Delete method to remove node at given index.
    def Delete(self, index):
        # Case for outside index range.
        if index > self.LengthLinkedList():
            print("Error: Index outside list")

        # Case for first index: Replace headpointer with second Node in list.
        elif index == 1:
            self.head = self.head.next

        # Case for all other indices: Delete the Node at index and link the Nodes behind and infront of the deleted Node.
        elif index > 1:
            CurrentNode = self.head
            CurrentIndex = 0

            while CurrentIndex < index - 1:
                TempNode = CurrentNode
                CurrentNode = CurrentNode.next
                CurrentIndex += 1
            TempNode.next = CurrentNode.next
            CurrentNode= None
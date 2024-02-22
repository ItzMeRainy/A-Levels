Stack = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 10 element stack, defined and initialized.
StackPointer = 0 # Pointer set to start of stack. Increments for every element added.

# Method to add number to stack.
def AddToStack():
    global StackPointer # Make sure stackpointer is set to global inside function/method.
    num = int(input("Enter a number to add: "))
    if StackPointer <= 9:
        Stack[StackPointer] = num
        StackPointer += 1
    else:
        print("Stack is Full")

# Method to remove number from stack.
def RemoveFromStack():
    global StackPointer # Make sure stackpointer is set to global inside function/method.
    if StackPointer >= 0:
        Stack[StackPointer - 1] = 0
        StackPointer -= 1
    else:
        print("Stack is Empty")
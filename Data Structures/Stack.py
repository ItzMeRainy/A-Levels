stack = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 10 element stack, defined and initialized.
global stackpointer # Make sure stackpointer is set to global outside and inside function/method.
stackpointer = 0 # Pointer set to start of stack

# Method to add number to stack.
def AddToStack():
    global stackpointer
    num = int(input("Enter a number to add: "))
    if stackpointer <= 9:
        stack[stackpointer] = num
        stackpointer += 1
    else:
        print("Stack is Full")

# Method to remove number from stack.
def RemoveFromStack():
    global stackpointer
    if stackpointer >= 0:
        stack[stackpointer - 1] = 0
        stackpointer -= 1
    else:
        print("Stack is Empty")
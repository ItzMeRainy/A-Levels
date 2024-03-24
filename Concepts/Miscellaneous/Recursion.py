def Factorial(number):
    if number == 0:
        return 1
    else:
        return number * Factorial(number - 1)
    
def FibonacciSequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = FibonacciSequence(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
    
print(FibonacciSequence(3))
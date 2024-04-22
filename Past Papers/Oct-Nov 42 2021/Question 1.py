# Part a)
def Unknown(X, Y):
    if X < Y:
        print(X + Y)
        return (Unknown(X + 1, Y) * 2)
    else:
        if X == Y:
            return 1
        else:
            print(X + Y)
            return (Unknown(X - 1, Y) // 2)

def IterativeUnknown(X, Y):
    counter = 0
    total = 1
    if X < Y:
        while X != Y:
            print(X + Y)
            X += 1
            counter += 1
        for x in range(counter):
            total *= 2
        return total

    elif X > Y:
        while X != Y:
            print(X + Y)
            X -= 1
            counter += 1
        for x in range(counter):
            total //= 2
        return total

    elif X == Y:
        return 1

x = 10
y = 15
print(x)
print(y)
print(Unknown(x, y))

x = 10
y = 10
print(x)
print(y)
print(Unknown(x, y))

x = 15
y = 10
print(x)
print(y)
print(Unknown(x, y))

x = 10
y = 15
print(x)
print(y)
print(IterativeUnknown(x, y))

x = 10
y = 10
print(x)
print(y)
print(IterativeUnknown(x, y))

x = 15
y = 10
print(x)
print(y)
print(IterativeUnknown(x, y))
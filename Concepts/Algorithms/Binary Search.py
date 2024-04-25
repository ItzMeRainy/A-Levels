def binarysearch(array, number):

    low = 0
    high = len(array) - 1

    while low <= high:
        middle = (low + high) // 2

        if array[middle] == number:
            return f"Number found at index: {middle}"
        elif number < array[middle]:
            high = middle - 1
        else:
            low = middle + 1
    
    return f"Number Not Found."

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binarysearch(mylist, 4))
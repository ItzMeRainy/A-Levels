def binarysearch(array, number):

    low = 0
    high = len(array)

    while low < high:
        middle = (high + low) // 2
        if array[middle] < number:
            low = middle + 1
        else:
            high = middle
    print(f"number \"{number}\" found at index \"{low}\"")
    return low

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binarysearch(mylist, 4)
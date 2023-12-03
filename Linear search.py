def linsearch(array):


    count = 0
    search = int(input("enter a number "))

    for i in range(1, len(array)):
       if search == array[i]:
            count = count + 1
            print("searched item found at index ", i + 1, ",", count, "time/times")

    if count == 0:
       print("item not found in list")

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
linsearch(array)


# A linear search is the simplest approach employed to search for an element in a data set.
# It examines each element until it finds a match, starting at the beginning of the data
# set, until the end. The search is finished and terminated once the target element is located.
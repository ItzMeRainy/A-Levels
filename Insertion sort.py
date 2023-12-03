def insertsort(list):


    sorted = 0 

    for count in range(0, len(list)):
        index = count

        while list[index - 1] > list[index] and index > 0:
            list[index], list[index - 1] = list[index - 1], list[index]
            index = index - 1

list = [-2, 2, 4, 6, 0, 8, 12, -3]
insertsort(list)
print(list)

# The lower part of an array is maintained to be sorted.
# An element which is to be 'insert'ed in this sorted sub-list, has to find its
# appropriate place and then it has to be inserted there. Hence the name, insertion sort.
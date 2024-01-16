def insertsort(list):
    for x in range(len(list)):
        sorting = x
        while sorting > 0 and list[sorting] < list[sorting - 1]:
            list[sorting], list[sorting - 1] = list[sorting - 1], list[sorting]
            sorting -= 1

list = [-2, 2, 4, 6, 0, 8, 12, -3]
insertsort(list)
print(list)

# The lower part of an array is maintained to be sorted.
# An element which is to be 'insert'ed in this sorted sub-list, has to find its
# appropriate place and then it has to be inserted there. Hence the name, insertion sort.
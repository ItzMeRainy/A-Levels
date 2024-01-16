def bubblesort(list):

    swaps = False

    for i in range(0, len(list)-1):
        for j in range(0, len(list)-1):

            if list[j] > list[j+1]:
                swaps = True
                list[j], list[j+1] = list[j+1], list[j]

        if swaps == False:
            return
        print(list)

list = [-2, 2, 4, 6, 0, 8, 12, -3]
bubblesort(list)

#Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly
#steps through the input list element by element, comparing the 
#current element with the one after it, swapping their values if needed.
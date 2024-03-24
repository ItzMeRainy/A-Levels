def bubblesort(list):

    swaps = False                                                             #This flag makes code stop the second no switch has occured

    for i in range(0, len(list)-1):                                           #No. of max iterations to be done
        for j in range(0, len(list)-1):                                       #This loop Compares every two adjacent values  

            if list[j] > list[j+1]:                                           #Swap
                swaps = True                                                  #Swap
                list[j], list[j+1] = list[j+1], list[j]                       #Swap

        if swaps == False:                                                    #Condition check
            return
        print(list)

list = [-2, 2, 4, 6, 0, 8, 12, -3]
bubblesort(list)

#Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly
#steps through the input list element by element, comparing the 
#current element with the one after it, swapping their values if needed.

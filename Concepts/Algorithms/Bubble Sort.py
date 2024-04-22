def bubblesort(list):
    for i in range(len(list)-1):                                           #No. of max iterations to be done
        swaps = False                                                         #This flag makes code stop the second no switch has occured

        for j in range(len(list)-1):                                       #This loop Compares every two adjacent values  
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
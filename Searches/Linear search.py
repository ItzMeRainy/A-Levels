def LinearSearch(List, Number):

   for i in range(len(List)):
      if Number == List[i]:
         print(f"'{Number}' found at index: {i}")
         return
      
   print("Number not found.")
   
MyList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
LinearSearch(MyList, 20)

# A linear search is the simplest approach employed to search for an element in a data set.
# It examines each element until it finds a match, starting at the beginning of the data
# set, until the end. The search is finished and terminated once the target element is located.
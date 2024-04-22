'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
'''

# Method 1:
with open('MyNumbers.txt', 'r') as Doc:
    pass

# Method 2:
Doc = open('MyNumbers.txt', 'r')
Doc.close()

'''
When using files, make sure you use Try Except blocks so the code runs even if the file is not found.

Use a print statement that outputs the error, like so:
'''

try:
    with open('MyNumbers.txt', 'r') as Doc:
        pass
except FileNotFoundError or IOError:
    print("File Not Found.")

'''
There are multiple ways to read data from a file.

1. Doc.readline() ---> This will read a single line from the file and return it.

2. Doc.readlines() ---> Reads all the lines in the file and returns them as a list. (Not recommended: Takes too much space in memory if file is too big.)

3. Doc.read() ---> Reads the entire file and returns it in the form of a single string. (Not recommended: Takes too much space in memory if file is too big.)
'''
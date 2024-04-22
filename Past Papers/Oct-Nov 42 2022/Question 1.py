Jobs = [[0, 0] for x in range(100)] # global array of type integer

def Initialise():
    global NumberOfJobs, Jobs
    for Job in Jobs:
        Job[0] = -1
        Job[1] = -1

    NumberOfJobs = 0

def AddJob(JobNumber, PriorityNumber):
    global NumberOfJobs, Jobs
    ThisJob = [JobNumber, PriorityNumber]
    if NumberOfJobs > 100:
        print('Not Added')
    else:
        Jobs[NumberOfJobs] = ThisJob
        NumberOfJobs += 1
        print('Added')

def InsertionSort():
    global NumberOfJobs, Jobs
    for x in range(NumberOfJobs):
        sorting = x
        while sorting > 0 and Jobs[sorting][1] < Jobs[sorting - 1][1]:
            Jobs[sorting], Jobs[sorting - 1] = Jobs[sorting - 1], Jobs[sorting]
            sorting -= 1

def PrintArray():
    for x in range(NumberOfJobs):
        print(f"{Jobs[x][0]} priority {Jobs[x][1]}")

# main
Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)

InsertionSort()
PrintArray()
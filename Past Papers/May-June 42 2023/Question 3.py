# Part a)
class Employee():
    #self.__HourlyPay single 
    #self.__EmployeeNumber string 
    #self.__JobTitle string

    def __init__(self, HourlyPay, EmployeeNumber, JobTitle):
        self.__EmployeeNumber = EmployeeNumber
        self.__HourlyPay = HourlyPay
        self.__JobTitle = JobTitle
        self.__PayYear2022 = [0.0 for i in range(52)]

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    
    def SetPay(self, WeekNum, HoursWorked):
        self.__PayYear2022[WeekNum - 1] = self.__HourlyPay * HoursWorked

    def GetTotalPay(self):
        TotalPay = 0

        for i in range(len(self.__PayYear2022)):
            TotalPay += self.__PayYear2022[i]

        return TotalPay
    
# Part b)
class Manager(Employee):
    #BonusValue single

    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, BonusValue):
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)
        self.__BonusValue = BonusValue

    def SetPay(self, WeekNum, HoursWorked):
        Hours = HoursWorked * (1 + self.__BonusValue / 100) 
        super().SetPay(WeekNum, Hours)

# Part c)
EmployeeArray = []   
Pay = 0.00 
ID = "" 
Bonus = 0.00 
Title = "" 
Temp = "" 
try: 
  TextFile = "Repos/A-Levels/Past Papers/May-June 42 2023/Papers/Employees.txt" 
  File = open(TextFile, 'r') 
  for x in range(0, 8): 
    Pay = float(File.readline()) 
    ID = File.readline() 
    Temp = File.readline() 

    try:   
        Bonus = float(Temp) 
        Title = File.readline() 
        EmployeeArray.append(Manager(Pay, ID, Title, Bonus)) 
    except: 
          Title = Temp 
          EmployeeArray.append(Employee(Pay, ID, Title))
    File.close

except IOError: 
    print("Could not find file")

# Part d)
def EnterHours():
    with open('Repos\A-Levels\Past Papers\May-June 42 2023\Papers\HoursWeek1.txt', 'r') as Doc:
        for Person in EmployeeArray:
            EmployeeID = Doc.readline()
            for x in range(8):
                if EmployeeArray[x].GetEmployeeNumber() == EmployeeID:
                    Person.SetPay(1, float(Doc.readline()))

EnterHours()
for Worker in EmployeeArray:
    print(Worker.GetEmployeeNumber(), Worker.GetTotalPay())
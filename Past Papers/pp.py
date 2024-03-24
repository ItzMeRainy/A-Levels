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
    
class Manager(Employee):
    #BonusValue single

    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, BonusValue):
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)
        self.__BonusValue = BonusValue

    def SetPay(self, WeekNum, HoursWorked):
        Hours = Hours * (1 + self.__BonusValue / 100) 
        super().SetPay(WeekNum, Hours)

EmployeeArray = []

with open("Repos\A-Levels\Past Papers\9618_s23_sf_42\06_9618_42_2023_source_files\Employees.txt", "w"):
    pass
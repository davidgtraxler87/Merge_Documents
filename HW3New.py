#David Traxler
#HW3


import os

class Payroll:
    def __init__(self, ID, Name, tHours, pHour, avg, pTotal, tDays):
        self.ID = ID # employee ID
        self.Name = Name #first name and last name concatenated
        self.tHours = tHours #total hours worked
        self.pHour = pHour #hourly rate
        self.avg = avg #avg hours worked
        self.pTotal = pTotal #salary
        #self.tDay = tDay #total days worked

fpath = "C:\Temp"

filePath = "C:\Temp\combinePayroll.txt"
lines = []
totalHours = 0.0
employee = []
PayrollList = []
writeString = ""
counter = 0

fileName1 = 'Payroll1.txt'
fileName2 = 'Payroll2.txt'
fullFileName1 = os.path.join(fpath, fileName1)
fullFileName2 = os.path.join(fpath, fileName2)


with open(fullFileName1, 'r') as infile1:
    lines1 = infile1.readlines()

with open(fullFileName2, 'r') as infile2:
    lines2 = infile2.readlines()

lines = lines1 + lines2

for line in lines:
    if (line.strip() == ""):
        continue
    columns = line.split()
    ID = columns[0]
    Name = columns[1] + ' ' + columns[2]
    pHour = float(columns[3])
    tHours = columns[4:]
    for hour in tHours:
        totalHours += float(hour)

    avg = totalHours / len(tHours)

    pTotal = totalHours * pHour
    # print (pTotal)
    Payroll = [Name, ID, pHour, totalHours, avg, pTotal]
    PayrollList.append(Payroll)
    totalHours = 0
    avg = 0
    tHours = []

ReportName = "Employee Payroll: "
marker = '-' * len(ReportName)
print(ReportName + ' \n' + marker)
for item in PayrollList:
    print("Payroll: {} ID {} worked {} hourly pay {} hours: {} / day Total Pay. ${} ". \
          format(item[0], item[1], item[2], item[3], item[4], item[5]))
    writeString += "Payroll: {} ID {} worked {} hourly pay {} hours: {} / day Total Pay. ${} \n". \
        format(item[0], item[1], item[2], item[3], item[4], item[5])

with open(filePath, 'w') as outFile:
    outFile.write(writeString)

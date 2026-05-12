from datetime import date
import math 

courseName = "DevOpsTTS2123"
classduration = 120 
courseduration = 0.75 
classStatus = True
classStart = date(2026, 3, 24)


#print(type(courseName))
#print(type(classduration))
#print(type(courseduration))
#print(type(classStatus))

#classDurationH = classduration /60
#print(int(classDurationH))

#print(date.today())

#today = date.today().strftime("%d-%m-%Y")
#print("Class Started on: ", classStart)

today = date.today()
print("Today is: ", today.strftime("%d-%m-%Y"))

difference = today - classStart

daysCompleted = difference.days
#weeksCompleted = daysCompleted / 7
weeksCompleted = round(daysCompleted / 7)
#weeksCompleted = math.ceil(daysCompleted / 7)
#weeksCompleted = math.floor(daysCompleted / 7)

print("Days from Class Start", daysCompleted)
print("Weeks from Class Start", weeksCompleted)
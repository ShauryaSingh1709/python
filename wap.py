#WAP to check if it is a weekend or not. If it is a weekend, then check if that person has woke up before 10 am or not. 
#If that person has woke up before 10 am, then print "Good Morning" else "Happy Weekend".
#If it is not a weekend, check if that person has worked for 8 hours or not. If he has worked for 8 hours, then print "His or Her Salary" else deduct 10000 from his or her salary and print the remaining salary. Salary is 20000.
Ndays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
Weekend = ("Saturday", "Sunday")
salary = 20000
day = input("Enter the day: ")
if day in Weekend:
    time = int(input("Enter the time you woke up (in 24-hour format): "))
    if time < 10:
        print("Good Morning")
    else:
        print("Happy Weekend")
else:
    hours = int(input("Enter the number of hours worked: "))
    if hours >= 8:
        print("Salary:-", salary)
    else:
        salary -= 10000
        print("Remaining Salary:", salary)
  
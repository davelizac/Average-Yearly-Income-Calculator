January = float(input("Enter your salary for January:\n"))
February = float(input("Enter your salary for February:\n"))
March = float(input("Enter your salary for March?:\n"))
April = float(input("Enter your salary for April:\n"))
May = float(input("Enter your salary for May:\n"))
June = float(input("Enter your salary for June:\n"))
July = float(input("Enter your salary for July:\n"))
August = float(input("Enter your salary for August:\n"))
September = float(input("Enter your salary for September:\n"))
October = float(input("Enter your salary for October:\n"))
November = float(input("Enter your salary for November:\n"))
December = float(input("Enter your salary for December:\n"))

months = [January, February, March, April, May, June, July, August, September, October,
         November, December]

sum_months = 0

for month in months:
  sum_months += month

average_yearly = 0

for salary in months:
  average_yearly += 1

result = round(sum_months / average_yearly, 2)


print(f"\n\nYour Average yearly income is: {result}") 


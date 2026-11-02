name = input("Enter Employee Name: ")
salary = float(input("Enter Basic Salary: "))

bonus = 2000
deduction = 1000

total_salary = salary + bonus
net_salary = total_salary - deduction
print("Employee Name:", name)
print("Basic Salary:", salary)
print("Bonus:", bonus)
print("Deduction:", deduction)
print("Net Salary:", net_salary)


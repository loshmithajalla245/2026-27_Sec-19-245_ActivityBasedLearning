days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
month = input("Enter month name: ")
total_days = int(input("Enter number of days: "))

print("   ", month")
for day in days:
    print(day, end=" ")
print()
for i in range(1, total_days + 1):
    print(i, end=" ")
 if i % 7 == 0:
        print()
   print()


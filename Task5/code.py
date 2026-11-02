total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

percentage = (attended / total) * 100

print("Attendance Percentage:", percentage)

if percentage >= 75:
    print("Attendance is Eligible")

else:
    needed = (0.75 * total - attended) / 0.25
    print("Attendance is Below 75%")
    print("Extra Classes Needed:", int(needed) + 1)




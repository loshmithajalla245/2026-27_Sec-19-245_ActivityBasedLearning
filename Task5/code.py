subject1 = input("Enter first subject: ")
time1 = input("Enter first subject time: ")
subject2 = input("Enter second subject: ")
time2 = input("Enter second subject time: ")
if time1 == time2:
    print("Timetable Conflict Detected!")
    print(subject1, "and", subject2, "have the same time.")

else:
    print("No Timetable Conflict.")
    print("Both subjects have different timings.")
total_classes = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

if total_classes > 0 and 0 <= attended <= total_classes:
    percentage = (attended / total_classes) * 100

    print("Attendance Percentage:", percentage, "%")

    if percentage >= 75:
        print("Attendance Status: Eligible")
    else:
        print("Attendance Status: Not Eligible")
else:
    print("Invalid attendance details.")



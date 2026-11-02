marks = [
    [80, 70, 90],
    [60, 75, 85],
    [90, 95, 80]
]

for i in range(3):
    total = sum(marks[i])
    print("Student", i+1)
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", total/3)
    print()




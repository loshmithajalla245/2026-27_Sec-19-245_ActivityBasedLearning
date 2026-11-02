name = input("Enter student name: ")
marks = float(input("Enter student marks (%): "))
income = float(input("Enter annual family income: "))
if marks >= 90 and income <= 200000:
    print("Congratulations!", name)
    print("You are eligible for a 100% scholarship.")

elif marks >= 80 and income <= 300000:
    print("Congratulations!", name)
    print("You are eligible for a 75% scholarship.")

elif marks >= 70 and income <= 500000:
    print("Congratulations!", name)
    print("You are eligible for a 50% scholarship.")

elif marks >= 60 and income <= 600000:
    print("Congratulations!", name)
    print("You are eligible for a 25% scholarship.")

else:
    print("Sorry!", name)
    print("You are not eligible for a scholarship.")




name = input("Enter Customer Name: ")
price = float(input("Enter Product Price: "))
quantity = int(input("Enter Quantity: "))

total = price * quantity
if total >= 5000:
    discount = total * 0.20
elif total >= 3000:
    discount = total * 0.15
elif total >= 1000:
    discount = total * 0.10
else:
    discount = total * 0.05
print("Customer Name:", name)
print("Total Amount:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)



products = (
    ("Pen", 10),
    ("Book", 50),
    ("Bag", 500),
    ("Pencil", 5),
for product in products:
    print("Product:", product[0])
    print("Price: Rs.", product[1])
    print("Total Products:", len(products))

prices = [product[1] for product in products]

print("Highest Price:", max(prices))
print("Lowest Price:", min(prices))

print("Catalogue Audit Completed")


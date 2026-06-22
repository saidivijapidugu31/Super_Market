print("WELCOME TO SUPER MARKET")

total_bill = 0

while True:
    item = input("\nEnter Item Name: ")
    price = int(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    amount = price * quantity
    total_bill += amount

    print("Item Total =", amount)

    choice = input("Add another item? (yes/no): ")

    if choice.lower() != "yes":
        break

print("\n----- FINAL BILL -----")
print("Total Bill =", total_bill)
print("Thank You for Shopping!")

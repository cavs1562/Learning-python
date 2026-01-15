#clean functions have clear names and do one job

def calculate_total(price, quantity):
    return price * quantity

price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

total = calculate_total(price, quantity)
print("Total cost:", total)

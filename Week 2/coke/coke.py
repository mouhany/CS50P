price = 50
total_paid = 0
coins = [25, 10, 5]

while price > 0:
    print(f"Amount Due: {price}")
    pay = int(input("Insert Coin: "))
    if pay in coins:
        # Update price and total_paid for every valid transaction
        price = price - pay
        total_paid = total_paid + pay

if total_paid >= price:
    print(f"Change Owed: {total_paid - 50}")
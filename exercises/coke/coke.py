amount_due = 50
accepted_coins = (25, 10, 5)

while amount_due > 0:
    try:
        coin = int(input("Insert Coin: "))
    except ValueError:
        coin = 0

    if coin in accepted_coins:
        amount_due -= coin

    print(f"Amount Due: {max(amount_due, 0)}")

change = max(-amount_due, 0)
print(f"Change Owed: {change}")
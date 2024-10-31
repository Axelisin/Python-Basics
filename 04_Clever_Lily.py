age = int(input())
washer = float(input())
toy_price = int(input())

toys = 0
cash = 0
brother = 0

for bd in range(1, age + 1):
    if bd % 2 == 0:
        cash = cash + (bd * 5)
        brother += 1 # cash -= 1 
    else:
        toys += 1

      
sold_toys = toys * toy_price
total_cash = (sold_toys + cash) - brother

if total_cash >= washer:
    money_left = total_cash - washer
    print(f"Yes! {money_left:.2f}")
else:
    money_needed = washer - total_cash
    print(f"No! {money_needed:.2f}")

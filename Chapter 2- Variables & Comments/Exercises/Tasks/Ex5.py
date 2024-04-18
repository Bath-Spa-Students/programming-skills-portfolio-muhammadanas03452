budget_money = 50 #pounds
usb_sticks_price = 6 #pounds each

num_usb_sticks = budget_money // usb_sticks_price
last_budget = budget_money % usb_sticks_price

print("Number of USB Sticks that can buy is:",num_usb_sticks)
print("Remaining budget left is:",last_budget)


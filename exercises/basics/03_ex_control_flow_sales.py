# 03_ex_control_flow_sales.py

"""
You have a list of closed deals for the month.
You need to classify deals and extract insights about sales performance.
"""

deals = [1200, 4500, 800, 15000, 3000, 2200, 5000]

small_deals = 0
mid_deals = 0
high_deals = 0

for deal in deals:
    if deal < 2000:
        small_deals += 1
    elif deal < 5000:
        mid_deals += 1
    else:
        high_deals += 1

print("Summary")
print("-------")
print("Small deals:", small_deals)
print("Mid deals:", mid_deals)
print("High deals:", high_deals)

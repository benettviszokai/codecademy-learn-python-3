"""
Carly's Clippers

In this project, the task was to analyze sales data for a hair salon using Python.
We used lists containing hairstyle names, their prices, and weekly sales numbers
to calculate useful business metrics: the average haircut price, updated discounted
prices, total revenue from last week, and average daily revenue. We also created
a filtered list showing only the haircuts priced under $30. This exercise practiced
loops, list comprehensions, indexing, and basic arithmetic to support real-world
data analysis.
"""

# Initial variables
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

# Calculating the total price
for price in prices:
  total_price += price

# Calculating the average price
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

# Creating a new price list (-5$ each)
new_prices = [price - 5 for price in prices]

# Calculating the revenue (prices * last week)
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("Total revenue: " + str(total_revenue))

# Calculating the average daily revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Creating a "Cuts under 30$" list
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)

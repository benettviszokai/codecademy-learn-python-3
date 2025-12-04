"""
Len's Slice

In this project, the task was to organize sales data for a pizza shop using Python
lists. We created lists to track pizza toppings and their prices, combined them
into a two-dimensional list, and then sorted and sliced that data to answer
practical questions like finding the cheapest and most expensive pizzas. Along
the way, we practiced counting values, measuring list length, sorting,
modifying list contents, and extracting subsets of data.
"""

# Toppings and prices:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# Counting the $2 slices
prices.count(2)

# Length of toppings
num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# Creating a 2D list of toppings and prices
pizza_and_prices = [
  [prices[0], toppings[0]],
  [prices[1], toppings[1]],
  [prices[2], toppings[2]],
  [prices[3], toppings[3]],
  [prices[4], toppings[4]],
  [prices[5], toppings[5]],
  [prices[6], toppings[6]]
]

# Sorting by price
pizza_and_prices.sort()

# Selecting the first element (cheapest pizza)
cheapest_pizza = pizza_and_prices[0]

# Selecting the last element (the most expensive pizza)
priciest_pizza = pizza_and_prices[-1]

# Removing the last element
pizza_and_prices.pop()

# Adding "peppers" pizza with the price of 2.5
pizza_and_prices.insert(4, [2.5, "peppers"])

# The tree lowest cost pizzas
three_cheapest = pizza_and_prices[:3]

print(pizza_and_prices)

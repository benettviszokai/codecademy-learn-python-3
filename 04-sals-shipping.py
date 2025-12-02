"""
Sal's Shipping

In this project, the task was to write a program that determines the cheapest
shipping method for a package based on its weight. Sal’s Shippers offers three
options—Ground Shipping, Ground Shipping Premium, and Drone Shipping—each with
different pricing rules. The program calculates the cost for each method and
outputs the most affordable choice. This exercise practices conditionals,
functions, and basic arithmetic in Python.
"""

# Weight
weight = 4.8

# Ground shipping cost calculation
ground_shipping_flat_charge = 20

if weight <= 2:
  cost_ground = 1.50 * weight + ground_shipping_flat_charge
elif weight > 2 and weight <= 6:
  cost_ground = 3.00 * weight + ground_shipping_flat_charge
elif weight > 6 and weight <= 10: 
  cost_ground = 4.00 * weight + ground_shipping_flat_charge
else:
  cost_ground = 4.75 * weight + ground_shipping_flat_charge

# Ground shipping premium cost calculation
cost_ground_premium = 125

# Drone shipping cost calculation
if weight <= 2:
  cost_drone = 4.50 * weight
elif weight > 2 and weight <= 6:
  cost_drone = 9.00 * weight
elif weight > 6 and weight <= 10: 
  cost_drone = 12.00 * weight
else:
  cost_drone = 14.25 * weight

# Output
print("Ground shipping price: " + str(cost_ground) + "$")
print("Ground shipping premium price: " + str(cost_ground_premium) + "$")
print("Drone shipping price: " + str(cost_drone) + "$")
print("Cheapest option: " + str(min(cost_ground, cost_ground_premium, cost_drone)) + "$")

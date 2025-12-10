"""
Time Traveler's Toolkit

In this project, the task was to create a Python script that simulates a playful
"time travel" experience using various Python modules. The goal was to build a
custom module, work with dates and times, perform precise calculations, use
random selection to choose destinations or eras, and finally generate a
personalized time travel message. This exercise brought together modular design,
datetime handling, math operations, and randomness to create a fun, themed program.
"""

# time_travelers_toolkit.py
import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

current_date = dt.date.today()
current_time = dt.datetime.now().time()

print(f"Current date is {current_date} and the current time is {current_time}.")

base_cost = Decimal('1000.00')
current_year = current_date.year
start_year = -2000
end_year = 3500
target_year = randint(start_year, end_year)
cost_multiplier = abs(current_year - target_year)
final_cost = round(base_cost * cost_multiplier, 2)

destinations = ["Egypt", "Europe", "America", "The Moon", "Future Mars Colony", "China", "London", "20,000 Leagues Under The Sea"]
selected_destination = choice(destinations)

print(custom_module.generate_time_travel_message(target_year, selected_destination, final_cost))

# custom_module.py
def generate_time_travel_message(year, destination, cost):
  return "Pack your bags! You're traveling to {destination} in the year {year}. The cost of this trip will be ${cost}.".format(year = year, destination = destination, cost = cost)

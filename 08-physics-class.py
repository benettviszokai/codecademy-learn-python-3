"""
Getting Ready for Physics Class

In this project, the task was to create a set of physics helper functions for
students to use when calculating basic physical properties. We wrote functions
to convert temperatures between Fahrenheit and Celsius, compute force,
calculate energy using E = mc^2, and determine work from force and distance.
The project focused on function definitions, parameters, default arguments,
return values, and applying scientific formulas in Python.
"""

# Initial variables
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Fahrenheit to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)

# Celsius to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Use the Force
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c=3*10**8):
  return mass * c ** 2

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Do the Work
def get_work(mass, acceleration, distance):
  result = get_force(mass, acceleration) * distance
  return result

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

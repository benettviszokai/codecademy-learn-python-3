"""
Python Code Challenges: Control Flow

In this set of challenges, the task was to practice Python control flow and
functions by solving a series of small, focused problems. Each exercise involved
using conditionals, logical operators, and function definitions to implement the
required behavior. The goal was not only to arrive at the correct solution, but
also to iterate, debug, and refine the code based on the output in order to
build a deeper understanding of how control flow works in Python.
"""

# 1. Not Sum To Ten
# You are given two numbers stored in num1 and num2. If the sum of num1 and num2 is NOT equal to 10, then store True into a variable called not_ten, otherwise store False in not_ten.

num1 = 6
num2 = 3

# Write your if statement here
if num1 + num2 != 10:
  not_ten = True
else:
  not_ten = False

# Uncomment the below lines to show the result
print("Is the sum of the numbers not equal to 10? " + str(not_ten))

# 2. Over Budget
# You are given a monthly budget and some expenses and need to check if the sum of the expenses goes over budget! First, store the total of all expenses into a variable called total. Next, check if the total is greater than the budget. If it is, store True into a variable called over_budget, otherwise store False in over_budget.

# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculate the total amount of expenses
total = food_bill + electricity_bill + internet_bill + rent

# Check if the total is greater than the budget and store the result in over_budget
if total > budget:
  over_budget = True
else:
  over_budget = False

# Uncomment the below lines to see the results

print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))

# 3. Large Power
# Create a function named large_power() that takes two parameters named base and exponent. If base raised to the exponent is greater than 5000, return True, otherwise return False

# Write your large_power function here:
def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False

# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

# 4. Twice As Large
# Create a function named twice_as_large() that has two parameters named num1 and num2. Return True if num1 is more than double num2. Return False otherwise.

# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if num1 > (num2 * 2): 
    return True
  else:
    return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

# 5. Divisible By Ten
# Create a function called divisible_by_ten() that has one parameter named num. The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.

# Write your divisible_by_ten() function here:
def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False

# Uncomment these print() function calls to test your divisible_by_ten() function:

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

"""
Control Flow (Advanced)

In this set of challenges, the task was to practice writing more advanced Python
functions that rely heavily on control flow. Each problem required using
conditionals, logical operators, and structured decision-making to implement the
desired behavior. The focus was on tackling harder problems, analyzing incorrect
output, iterating on solutions, and deepening understanding of how complex
control flow can be modeled in Python.
"""

# 1. In Range
# Create a function named in_range() that has three parameters named num, lower, and upper. The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.

# Write your in_range function here:
def in_range(num, lower, upper):
  if (num >= lower) and (num <= upper):
    return True
  else:
    return False

# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

# 2. Same Name
# Create a function named same_name() that has two parameters named your_name and my_name. If our names are identical, return True. Otherwise, return False.

# Write your same_name function here:
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False

# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

# 3. Always False
# Create a function named always_false() that has one parameter named num. Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num. An if statement that is always false is called a contradiction. You will rarely want to do this while programming, but it is important to realize it is possible to do this.

# Write your always_false function here:
def always_false(num):
  if (num < 0) and (num > 0):
    return True
  else:
    return False

# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

# 4. Movie Review
# Create a function named movie_review() that has one parameter named rating. If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"

# Write your movie_review function here:
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating < 9:
    return "This was fun!"
  else:
    return "Outstanding!"

# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

# 5. Max Number
# Create a function called max_num() that has three parameters named num1, num2, and num3. The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!".

# Write your max_num function here:
def max_num(num1, num2, num3):
  if (num1 > num2) and (num1 > num3):
    return num1
  elif (num2 > num1) and (num2 > num3):
    return num2
  elif (num3 > num1) and (num3 > num2):
    return num3
  else:
    return "It's a tie!"

# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"

"""
Python Code Challenges: Lists

In this set of challenges, the task was to practice working with Python lists by
solving a series of small problems using functions. Each exercise focused on
operations such as indexing, slicing, iterating over lists, modifying list
contents, and returning new lists based on certain conditions. The goal was to
experiment, debug, and refine solutions while building a stronger understanding
of how to manipulate lists effectively in Python.
"""

# 1. Append Size

# Create a function called append_size() that has one parameter named my_list.
# The function should append the size of my_list (inclusive) to the end of my_list. The function should then return this new list.
# For example, if my_list was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of my_list was originally 3.

# Write your function here
def append_size(my_list):
  my_list.append(len(my_list))
  return my_list

# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

# 2. Append Sum

# Write a function named append_sum() that has one parameter — a list named named my_list.
# The function should add the last two elements of my_list together and append the result to my_list. It should do this process three times and then return my_list.
# For example, if my_list started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

# Write your function here
def append_sum(my_list):
  last_two = my_list[-1] + my_list[-2]
  my_list.append(last_two)
  last_two = my_list[-1] + my_list[-2]
  my_list.append(last_two)
  last_two = my_list[-1] + my_list[-2]
  my_list.append(last_two)
  
  return my_list

# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

# 3. Larger List

# Write a function named larger_list() that has two parameters named my_list1 and my_list2.
# The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of my_list1.

# Write your function here
def larger_list(my_list1, my_list2):
  if len(my_list1) > len(my_list2):
    return my_list1[-1]
  elif len(my_list1) < len(my_list2):
    return my_list2[-1]
  else:
    return my_list1[-1]

# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# 4. More Than N

# Create a function named more_than_n() that has three parameters named my_list, item, and n.
# The function should return True if item appears in the list more than n times. The function should return False otherwise.

# Write your function here
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False

# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# 5. Combine Sort

# Write a function named combine_sort() that has two parameters named my_list1 and my_list2.
# The function should combine these two lists into one new list and sort the result. Return the new sorted list.

# Write your function here
def combine_sort(my_list1, my_list2):
  newlist = my_list1 + my_list2
  newlist.sort()
  return newlist


# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

"""
Python Code Challenges: Loops

In this set of challenges, the task was to practice using Python loops by solving
a series of focused problems. Each exercise involved applying for and while
loops to iterate over data, accumulate results, and control the flow of repeated
operations. The goal was to write, test, debug, and refine loop-based solutions
in order to build confidence and fluency with iteration in Python.
"""

# 1. Divisible By Ten

# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
# Return the count of how many numbers in the list are divisible by 10.

#Write your function here
def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

# 2. Greetings

# Create a function named add_greetings() which takes a list of strings named names as a parameter.
# In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name in names and append the greeting to the list.
# Return the new list containing the greetings.

#Write your function here
def add_greetings(names):
  greeting = []
  for name in names:
    greeting.append('Hello, ' + name)
  return greeting

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

# 3. Delete Starting Even Numbers

# Write a function called delete_starting_evens() that has a parameter named my_list.
# The function should remove elements from the front of my_list until the front of the list is not even. The function should then return my_list.
# For example if my_list started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(my_list) should return [11, 12, 15].
# Make sure your function works even if every element in the list is even!

#Write your function here
def delete_starting_evens(my_list):
  while (len(my_list) > 0 and my_list[0] % 2 == 0):
    my_list = my_list[1:]
  return my_list

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# 4. Odd Indices

# Create a function named odd_indices() that has one parameter named my_list.
# The function should create a new empty list and add every element from my_list that has an odd index. The function should then return this new list.
# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

#Write your function here
#Write your function here
def odd_indices(my_list):
  new_list = []
  for index in range(1, len(my_list), 2):
    new_list.append(my_list[index])
  return new_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

# 5. Exponents

# Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

#Write your function here
def exponents(bases, powers):
  newlist = []
  for i in bases:
    for j in powers:
      newlist.append(i ** j)
  return newlist

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

"""
Python Code Challenges: Loops (Advanced)

In this set of challenges, the task was to practice advanced use of Python loops
by solving more difficult, loop-heavy problems. Each exercise focused on
techniques such as nested loops, complex iteration patterns, and careful control
of loop execution to produce the correct results. The goal was to write, test,
and refine solutions while deepening understanding of how to use loops to handle
non-trivial logic and data processing in Python.
"""

# 1. Larger Sum

# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

#Write your function here
def larger_sum(lst1, lst2):
  newlist1 = 0
  newlist2 = 0
  for i in lst1:
    newlist1 += i
  for j in lst2:
    newlist2 += j
  if newlist1 > newlist2 or newlist1 == newlist2:
    return lst1
  else:
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

# 2. Over 9000

# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.
# The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.
# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

#Write your function here
def over_nine_thousand(lst):
  sum = 0
  
  if len(lst) == 0:
    return 0
  else:
    for i in lst:
      sum += i
      if sum > 9000:
        break
    return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

# 3. Max Num

# Create a function named max_num() that takes a list of numbers named nums as a parameter.
# The function should return the largest number in nums

#Write your function here
def max_num(nums):
  return max(nums)

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

# 4. Same Values

# Write a function named same_values() that takes two lists of numbers of equal size as parameters.
# The function should return a list of the indices where the values were equal in lst1 and lst2.

#Write your function here
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# 5. Reversed list

# Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.
# The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.
# For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

#Write your function here
def reversed_list(lst1, lst2):
  lst2.sort()
  if lst1 == lst2:
    return True
  else:
    return False

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

"""
Python Code Challenges: Functions

In this set of challenges, the task was to practice writing and using Python
functions by solving a variety of small problems. Each exercise focused on
defining functions with parameters, returning values, and applying logic inside
the function body to meet specific requirements. The goal was to experiment,
debug, and iterate on solutions in order to build a stronger understanding of
how to design and work with functions in Python.
"""

# 1. Tenth Power

# Write a function named tenth_power() that has one parameter named num.
# The function should return num raised to the 10th power.

# Write your tenth_power function here:
def tenth_power(num):
  return num ** 10

# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

# 2. Square Root

# Write a function named square_root() that has one parameter named num.
# Use exponents (**) to return the square root of num.

# Write your square_root function here:
def square_root(num):
  return num ** 0.5

# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

# 3. Win Percentage

# Create a function called win_percentage() that takes two parameters named wins and losses.
# This function should return out the total percentage of games won by a team based on these two numbers.

# Write your win_percentage function here:
def win_percentage(wins, losses):
  return (wins / (wins + losses)) * 100

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

# 4. Average

# Write a function named average() that has two parameters named num1 and num2.
# The function should return the average of these two numbers.

# Write your average function here:
def average(num1, num2):
  return (num1 + num2) / 2

# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

# 5. Remainder

# Write a function named remainder() that has two parameters named num1 and num2.
# The function should return the remainder of twice num1 divided by half of num2.

# Write your remainder function here:
def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)

# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

"""
Python Code Challenges: Functions (Advanced)

In this set of challenges, the task was to practice writing more advanced Python
functions by solving difficult, function-focused problems. Each exercise required
careful use of parameters, return values, and control flow inside functions to
implement the desired behavior. The goal was to tackle harder problems, debug
and refine solutions based on their output, and deepen understanding of how to
design, structure, and reason about complex functions in Python.
"""

# 1. First Three Multiples

# Write a function named first_three_multiples() that has one parameter named num.
# This function should print the first three multiples of num. Then, it should return the third multiple.
# For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.

# Write your first_three_multiples function here
def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

# 2. Tip

# Create a function called tip() that has two parameters named total and percentage.
# This function should return the amount you should tip given a total and the percentage you want to tip.

# Write your tip function here:
def tip(total, percentage):
  return (total * percentage) / 100

# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

# 3. Bond, James Bond

# Write a function named introduction() that has two parameters named first_name and last_name.
# The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.

# Write your introduction function here:
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

# 4. Dog Years

# Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named dog_years() that has two parameters named name and age.

# Write your dog_years function here:
def dog_years(name, age):
  return name + ", you are " + str(age * 7) + " years old in dog years"

# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

# 5. All Operations

# Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.
# First, print the sum of a and b.
# Second, print c minus d.
# Third, print the first number printed, multiplied by the second number printed.
# Finally, return the third number printed modulo a.

# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
  first = a + b
  print(first)
  second = c - d
  print(second)
  third = first * second
  print(third)
  return third % a

# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

"""
Gradebook

In this project, the task was to organize school subjects and grades using Python
lists. The goal was to create and modify a two-dimensional list (a gradebook)
containing subjects and their corresponding scores. Throughout the exercise,
we practiced list creation, appending new entries, updating values, removing
items, and combining lists to build a complete gradebook.
"""

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Creating the initial gradebook: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Adding more subjects
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Modifying data
gradebook[5][1] += 5
gradebook[2].remove(85)
gradebook[2].append("Pass")

# Combining lists
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)

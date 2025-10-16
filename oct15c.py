'''
# ⿢ BAR GRAPH
# ------------------------------------------------------------
# Q3: Create a bar chart showing the number of students enrolled in each course.
# courses = ['AI', 'ML', 'Data Science', 'Web Dev']
# students = [50, 40, 60, 30]
# - Label the x and y axes
# - Add different colors for each bar

'''

import matplotlib.pyplot as plt
import numpy as np

courses = np.array(['AI', 'ML', 'Data Science', 'Web Dev'])
students = np.array([50, 40, 60, 30])
plt.xlabel("courses")
plt.ylabel("students")

plt.bar(courses,students,color = ("green","yellow","blue","black"))
plt.show()
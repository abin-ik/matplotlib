import matplotlib.pyplot as plt
import numpy as np

''' 
Standard deviation = spread or deviation from mean value

'''

"""
corelation is the relationship between two variables
if v1 increases v2 also increases - positive corelation
if v1 increases v2 decreases - neagtive corelation

"""

x = np.random.normal(loc=20,scale=15,size=100)
x = np.clip(x,0,85)

plt.hist(x)

plt.show()
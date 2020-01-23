import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np


# a list of items 
data = [['Alex',10],['Bob',12],['Clarke',13]]
#using pandas to arrange the data
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)

print ("hello world")

print (df)

# Create data
N = 10                # Definition for dimensions, specifies the amount of returned random values
x = np.random.rand(N)   # Define random x value
y = np.random.rand(N)   # Define random y value 
area = np.pi*1         # Define the area of the points

# Plot
plt.scatter(x, y, s=area, c='black', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')

#arbitary plotting
# plt.plot([1,2,3,5,8],[3,4,2,1,6])

# plt.plot()

plt.show()
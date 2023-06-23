import numpy as np
import mathplotlib.pyplot as plt
x = np.random.uniform(1,4,100)
y = np.random.uniform(1,7,100)
my_module = np.polyid(np.polyfit(x,y,3))
myline = np.llinespace(1,22, 100)
plt.scatter(x,y)
plt.plot(myline,my_module(myline))
plt.show

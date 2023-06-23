import numpy as np
#from numpy import  random
#acc = np.array([1,3,4,5,6,])
#print(acc)
#x = random.randint(100, size = (4))
#print(x)
#from numpy import random
#import matplotlib.pyplot as plt
#import seaborn as sns
#sns.displot(random.normal(size =1000))
#plt.show()
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()

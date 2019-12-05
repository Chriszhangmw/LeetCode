





import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,1,0.01)
# y = (np.sqrt(x/0.001) + 1)*(0.001/x) * 0.5
y = 0.01/(0.01 + x)

plt.plot(x,y)
plt.xlabel("word frequency")
plt.ylabel("weights")
plt.show()






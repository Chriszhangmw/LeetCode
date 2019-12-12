





import numpy as np
import matplotlib.pyplot as plt
axes = plt.gca()
axes.set_ylim([0,1])
x = np.arange(0,1,0.01)
plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
y1 = (np.sqrt(x/0.1) + 1)*(0.1/x) * 0.5
y2 = (np.sqrt(x/0.01) + 1)*(0.01/x) * 0.5
y3 = (np.sqrt(x/0.001) + 1)*(0.001/x) * 0.5
y4 = (np.sqrt(x/0.0001) + 1)*(0.0001/x) * 0.5

# y1 = 0.1/(0.1 + x)
# y2 = 0.01/(0.01 + x)
# y3 = 0.001/(0.001 + x)
# y4 = 0.0001/(0.0001 + x)
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.xlabel("Z(wi),word frequency")
plt.ylabel("weights")
# plt.legend([' α = 0.1', 'α = 0.01', 'α = 0.001', 'α = 0.0001'], loc='upper left')
plt.legend([' β = 0.1', 'β = 0.01', 'β = 0.001', 'β = 0.0001'], loc='upper left')
plt.show()






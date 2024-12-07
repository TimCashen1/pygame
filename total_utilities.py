import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

time=np.array(["September","October","November","December","January","February","March","April","May","June"])
total_cost=np.array([83.98,88.53,95.88,86.21000000000001,102.27000000000001,93.25999999999999,147.73,183.69,137.74,53.769999999999996])

plt.figure(figsize=(10,5))
plt.plot(time,total_cost,'-', linewidth=2, markersize=10,label='Total Cost')
plt.xlabel('Months')
plt.ylabel('Price ($)')
plt.title('Utility Costs')
plt.legend()

plt.show()


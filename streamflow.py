import matplotlib.pyplot as plt
import numpy as np

array1 = np.genfromtxt('June-2021-Provo-River-Streamflow-Rates (1).csv', delimiter=',',dtype=str,skip_header=1)
x = array1[:,0].astype('datetime64')
y_1 = array1[:,1].astype(float)
y_2 = array1[:,2].astype(float)
y_3 = array1[:,3].astype(float)
y_4 = array1[:,4].astype(float)
y_5 = array1[:,5].astype(float)

plt.figure(figsize=(12, 6))
plt.plot(x, y_1, label='Site 10163000', color='red', linewidth=2)
plt.plot(x, y_2, label='Site 10155200', color='blue', linewidth=2)
plt.plot(x, y_3, label='Site 10155500', color='orange', linewidth=2)
plt.plot(x, y_4, label='Site 10154200', color='green', linewidth=2)
plt.plot(x, y_5, label='Site 10155000', color='purple', linewidth=2)
plt.xlabel('Date')
plt.ylabel('Streamflow')
plt.title('Streamflow Data for Provo River')
plt.grid(True)
plt.legend()
plt.show()

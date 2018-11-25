import matplotlib.pyplot as plt
import csv
import numpy
x = []
y = []

filename = "data_*.csv"
with open(filename,'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        x.append(int(row[0]))
print(x)
# plt.plot(x,y, label='Loaded from file!')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
# plt.show()
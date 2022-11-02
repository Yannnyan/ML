import math

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
import datasetCreate as data


def load_dataset():
    data_set = []
    with open(data.filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) != 0:
                data_set.append(row)
    return data_set


plt.rcParams["figure.figsize"] = [7.00, 5.50]
plt.rcParams["figure.autolayout"] = True
x = [4]
y = [3]
plt.xlim(0, 20)
plt.ylim(0, 20)
plt.grid()
data_set = load_dataset()
print(data_set)
for row in data_set:
    color = 'green' if row[2] == '1' else 'red'
    if row[0] != 'x':
        plt.plot(int(row[0]), int(row[1]), marker="o", markersize=4, markeredgecolor=color, markerfacecolor=color)
plt.show()
import csv
import random


def save_results(arr, filename):
    with open(filename, 'w') as f:
        write = csv.writer(f)
        write.writerow(['x', 'y', 'color'])
        for row in arr:
            write.writerow(row)


filename = 'savedresults.csv'
arr = []
for i in range(20):
    color = random.randint(0, 1)
    x = random.randint(1, 19)
    y = 0
    if color == 0:
        y = random.randint(1, 10)
    else:
        y = random.randint(10, 19)

    arr.append([x, y, color])
save_results(arr, filename)

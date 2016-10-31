from random import randint
from datetime import datetime

startTime = datetime.now()

my_num = []
for number in range(1, 101):
    my_num.append(randint(1, 10001))

def bubbleSort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
bubbleSort(my_num)

print(my_num)

print datetime.now() - startTime
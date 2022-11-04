'''
Task №4

There is an array of numbers - arr [1, 3, 6, 2, 2, 0, 4, 5] 
there is a number target = 5.
Count the number of pairs in the array, the sum of which will give target
'''
import numpy as np


def task(arr : list, target : int):
    res = 0

    for i in arr:
        for j in arr:
            if i + j == target and i != j:
                res += 1

    return res // 2


arr = [1, 3, 6, 2, 2, 0, 4, 5]
target = 5

print(task(arr, target))
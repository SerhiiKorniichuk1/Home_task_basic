'''
Task №3

Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer.
'''
import math 

def digital_root(n):
    sum = 0
    x = [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
    for y in x:
        sum += y
    return sum
